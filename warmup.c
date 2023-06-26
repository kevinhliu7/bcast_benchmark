#include <stdlib.h>
#include <stdio.h>
#include "mpi.h"

// perform 1000 bcasts to warmup machine

int main(int argc, char** argv) {
    int rank;
    int num_procs;
    int number = 5;

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &num_procs);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    
    for (int i = 0; i < 1000; i++) {
        MPI_Bcast(&number, 1, MPI_INT, 0, MPI_COMM_WORLD);
    }
    MPI_Finalize();
    return 0;
}