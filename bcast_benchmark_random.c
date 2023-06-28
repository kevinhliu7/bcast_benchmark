#include <stdlib.h>
#include <stdio.h>
#include "mpi.h"

int main(int argc, char** argv) {
    FILE* fptr = fopen("/scratch/test-mpi-build/bcast_benchmark/results_random.txt", "a");
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
    
    int num_nodes = atoi(getenv("SLURM_JOB_NUM_NODES"));
    //int color = rank % num_nodes; // color = rank % Number of Nodes This part is wrong all processes should still belong to the same communicator
    //int key = rank; // key = rank
    srand(time(NULL));
    int color = 0;
    int key = rand() % num_nodes;

    // does SLURM allocate a communicator to every node???

    MPI_Comm new_comm; // new communicatior for the subgroup
    MPI_Comm_split(MPI_COMM_WORLD, color, key, &new_comm);
    int new_rank;
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