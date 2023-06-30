#include <stdio.h>
#include <stdlib.h>
#include "mpi.h"


int main(int argc, char** argv) {
    
    int rank, numprocs;
    char msg = 'A';
    FILE* fptr = fopen("/scratch/test-mpi-build/bcast_benchmark/latency.txt", "a");

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &numprocs);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    
    MPI_Status status;
    
    // intended to warmup the machine
    int error_num;
    
    for (int i = 0; i < 1000; i++) {
        error_num = MPI_Sendrecv(&msg, 1, MPI_CHAR, 1, 0, &msg, 1, MPI_CHAR, 0, 1, MPI_COMM_WORLD, &status);
    }
    
    double start_time = MPI_Wtime();
    for (int i = 0; i < 10000; i++) {
        error_num = MPI_Sendrecv(&msg, 1, MPI_CHAR, 1, 0, &msg, 1, MPI_CHAR, 0, 1, MPI_COMM_WORLD, &status);
    }
    double end_time = MPI_Wtime();
    
    double duration = (end_time - start_time) / 10000;


    

    MPI_Allreduce();


    MPI_Finalize();
    
    return 0;
}