#include <stdlib.h>
#include <stdio.h>
#include "mpi.h"

#define ROUNDS 5 
#define ITERATIONS 1000000
int main(int argc, char** argv) {

    char* hier_or_bcast = getenv("MPIR_CVAR_BCAST_INTRA_ALGORITHM");
    
    FILE* fptr;
    if (hier_or_bcast[0] == 'b') {
        fptr = fopen("/gpfs/fs1/home/kliu/job_submissions/bcast_benchmark/results_random.txt", "a");
    } else {
        fptr = fopen("/gpfs/fs1/home/kliu/job_submissions/bcast_benchmark/results_hier_random.txt", "a");
    }

    int rank;
    int num_procs;
    int number = 5;
    //double time_single_bcast_true = -1;
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
    srand(MPI_Wtime());
    int color = 0;
    int key = rand() % num_nodes;

    MPI_Comm new_comm; // new communicatior for the subgroup
    MPI_Comm_split(MPI_COMM_WORLD, color, key, &new_comm);
    int new_rank;
    MPI_Comm_rank(new_comm, &new_rank);
    
    
    // warmup the machine
    for (int i = 0; i < ITERATIONS; i++) {
        MPI_Bcast(&number, 1, MPI_INT, 0, new_comm);
    }
    
    double* times = (double*) malloc(sizeof(double) * ROUNDS);

    for (int num_rounds = 0; num_rounds < ROUNDS; num_rounds++) {

        double time_begin = MPI_Wtime();
        for (int i = 0; i < ITERATIONS; i++) {
            MPI_Bcast(&number, 1, MPI_INT, 0, new_comm);
        }
        double time_end = MPI_Wtime();

        // find the average time to get the time of a single bcast
        double time_single_bcast = (time_end - time_begin) / ITERATIONS;

        times[num_rounds] = time_single_bcast;
        
    }
    
    // Bubblesort the array in ascending order
    for (int i = 0; i < ROUNDS; i++) {
        for (int j = 0; j < ROUNDS - 1; j++) {
            if (times[i] > times[i + 1]) {
                int tmp = times[i];
                times[i] = times[i + 1];
                times[i + 1] = tmp;
            }
        }
    }

    double Q1 = times[ROUNDS / 4];
    double Q3 = times[(ROUNDS * 3) / 4];
    double IQR = Q3 - Q1;

    // remove outliers
    int num_valid = ROUNDS;
    double true_sum = 0;
    for (int i = 0; i < ROUNDS; i++) {
        if (times[i] >= 1.5 * IQR) {
            times[i] = 0;
            num_valid--;
        } else {
            true_sum += times[i];
        }
    }
    double true_average = true_sum / num_valid;
    double real_time = -1;

    free(times);

    MPI_Allreduce(&true_average, &real_time, 1, MPI_DOUBLE, MPI_MAX, new_comm);

    // convert to microseconds
    real_time *= 1000000;

    if (!rank) {
        fprintf(fptr, "%lf\n", real_time);
        printf("Time: %lf\n", real_time);
    }
    MPI_Finalize();
    fclose(fptr);
    return 0;
}