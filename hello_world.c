#include <stdio.h>
#include <stdlib.h>
#include "mpi.h"

int main(int argc, char** argv) {
    int rank;
    int num_procs;
    int number = 5;
    double time_single_bcast_true = -1;

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &num_procs);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Bcast(&number, 1, MPI_INT, 0, MPI_COMM_WORLD);
    MPI_Finalize();
    if (!rank) {
        printf("Hello World! %d \n", num_procs);
    }

    return 0;
}