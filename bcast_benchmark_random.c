#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include "mpi.h"


#define ROUNDS 50 
#define ITERATIONS 100000
#define MSG_SIZE 4
int main(int argc, char** argv) {
    
    //double time_single_bcast_true = -1;
    char* hier_or_bcast = getenv("MPIR_CVAR_BCAST_INTRA_ALGORITHM");
    
    FILE* fptr;
    if (hier_or_bcast[0] == 'b') {
        fptr = fopen("/gpfs/fs1/home/kliu/job_submissions/bcast_benchmark/results_random.txt", "a");
    } else {
        fptr = fopen("/gpfs/fs1/home/kliu/job_submissions/bcast_benchmark/results_hier_random.txt", "a");
    }

    int rank;
    int num_procs;
    char* msg = (char*) malloc(sizeof(char) * MSG_SIZE);
    
    for (int i = 0; i < MSG_SIZE; i++) {
        msg[i] = '?';
    }
    
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
        MPI_Bcast(msg, MSG_SIZE, MPI_CHAR, 0, new_comm);
    }
    
    double* times = (double*) malloc(sizeof(double) * ROUNDS);

    for (int num_rounds = 0; num_rounds < ROUNDS; num_rounds++) {

        MPI_Barrier(new_comm);

        double time_begin = MPI_Wtime();
        for (int i = 0; i < ITERATIONS; i++) {
            MPI_Bcast(msg, MSG_SIZE, MPI_CHAR, 0, new_comm);
        }
        double time_end = MPI_Wtime();

        // find the average time to get the time of a single bcast
        double time_single_bcast = (time_end - time_begin) / ITERATIONS;

        double true_time_single_bcast = -1;

        MPI_Allreduce(&time_single_bcast, &true_time_single_bcast, 1, MPI_DOUBLE, MPI_MAX, new_comm);


        times[num_rounds] = true_time_single_bcast;
        
    }
    
    // Bubblesort the array in ascending order
    // for (int i = 0; i < ROUNDS; i++) {
    //     for (int j = 0; j < ROUNDS - 1; j++) {
    //         if (times[i] > times[i + 1]) {
    //             int tmp = times[i];
    //             times[i] = times[i + 1];
    //             times[i + 1] = tmp;
    //         }
    //     }
    // }

    // double Q1 = times[ROUNDS / 4];
    // double Q3 = times[(ROUNDS * 3) / 4];
    // double IQR = Q3 - Q1;

    // remove outliers
    // int num_valid = ROUNDS;
    // double true_sum = 0;
    // for (int i = 0; i < ROUNDS; i++) {
    //     if (times[i] >= 1.5 * IQR) {
    //         times[i] = 0;
    //         num_valid--;
    //     } else {
    //         true_sum += times[i];
    //     }
    // }
    // double true_average = true_sum / num_valid;
    // double real_time = -1;

    double sum = 0;
    
    for (int i = 0; i < ROUNDS; i++) {
        sum += times[i];
    }
    
    double mean = sum / ROUNDS;
    double var = 0;
    
    for (int i = 0; i < ROUNDS; i++) {
        var += (times[i] - mean) * (times[i] - mean);
    }

    var /= ROUNDS;

    free(times);
    free(msg);

    mean *= 1000000;
    var *= 1000000;

    if (!rank) {
        fprintf(fptr, "%lf %lf\n", mean, var);
        printf("Time: %lf; Stdev: %lf \n", mean, var);
    }
}