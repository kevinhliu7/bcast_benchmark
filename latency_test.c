#include <stdio.h>
#include <stdlib.h>
#include "mpi.h" 


int main(int argc, char** argv) {

    int rank, numprocs;
    char msg = 'A';
    FILE* fptr = fopen("/gpfs/fs1/home/kliu/job_submissions/bcast_benchmark/latency.txt", "a");

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &numprocs);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    MPI_Status status;

    // intended to warmup the machine
  
    int error_num;
    
    for (int i = 0; i < 1000000; i++) {
           if (!rank) {
                MPI_Send(&msg, 1, MPI_CHAR, 1, 0, MPI_COMM_WORLD);
           } else {
                MPI_Recv(&msg, 1, MPI_CHAR, 0, 0, MPI_COMM_WORLD, &status);
           }
    }

    double start_time = MPI_Wtime();
    
    for (int i = 0; i < 1000000; i++) {
           if (!rank) {
                MPI_Send(&msg, 1, MPI_CHAR, 1, 0, MPI_COMM_WORLD);
           } else {
                MPI_Recv(&msg, 1, MPI_CHAR, 0, 0, MPI_COMM_WORLD, &status);
           }
    }
    double end_time = MPI_Wtime();

    double duration = (end_time - start_time) / 1000000;

    double true_duration;

    MPI_Allreduce(&duration, &true_duration, 1, MPI_DOUBLE, MPI_MAX, MPI_COMM_WORLD);

    if (!rank) {
        printf("My latency is: %lf \n", true_duration * 1000000);
        fprintf(fptr, "%lf\n", true_duration * 1000000);
    }

    fclose(fptr);

    MPI_Finalize();

    return 0;
}
