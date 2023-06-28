#include <stdlib.h>
#include <stdio.h>
#include "mpi.h"

// int get_color(int size, int num_nodes, int rank) {
//     int PPN = size / num_nodes;
//     if (size > 2 && num_nodes > 1) {
//         int j = 2;
//         for  (int i = 0; i < num_nodes; i++) {
//             for (int k = 0; k < PPN; k++) {
//                 if (j == rank) {
//                     return i;
//                 }
//                 j = (j + 1) % size;
//             }
//         }
//     }
//     return -1;
// }

int main(int argc, char** argv) {
    FILE* fptr = fopen("/scratch/test-mpi-build/bcast_benchmark/results_shifted.txt", "a");
    int rank;
    int num_procs;
    int number = 5;
    double time_single_bcast_true = -1;
    if (!fptr) {
        printf("Could Not Open File \n");
        exit(1);
    }
    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &num_procs);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    
    int key = (rank + 2) % num_procs;
    int num_nodes = atoi(getenv("SLURM_JOB_NUM_NODES"));
    int new_rank;
    //int color = get_color(num_procs, num_nodes, rank); this part is wrong, all processes should still belong to the same communicator
    int color = 0;

    MPI_Comm new_comm;
    MPI_Comm_split(MPI_COMM_WORLD, color, key, &new_comm);
    MPI_Comm_rank(new_comm, &new_rank);

    //printf("My old rank was %d and now my new rank is %d \n", rank, new_rank);
    
    double time_begin = MPI_Wtime();
    for (int i = 0; i < 10000; i++) {
        MPI_Bcast(&number, 1, MPI_INT, 0, MPI_COMM_WORLD);
    }
    double time_end = MPI_Wtime();
    // find the average time to get the time of a single bcast
    double time_single_bcast = (time_end - time_begin) / 10000;

    MPI_Allreduce(&time_single_bcast, &time_single_bcast_true, 1, MPI_DOUBLE, MPI_MAX, MPI_COMM_WORLD);

    time_single_bcast_true *= 1000000;

    if (!rank) {
        fprintf(fptr, "%lf\n", time_single_bcast_true);
        printf("Time: %lf \n", time_single_bcast_true);
    }

    MPI_Finalize();
    fclose(fptr);
    return 0;
}