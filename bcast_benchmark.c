#include <stdlib.h>
#include <stdio.h>
#include "mpi.h"

// this program is meant to perform
// benchmarks on Bcast

// Currently, we are working with the original ordering of ranks

int main(int argc, char** argv) {
    FILE* fptr = fopen("/scratch/test-mpi-build/bcast_benchmark/results.txt", "a");
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