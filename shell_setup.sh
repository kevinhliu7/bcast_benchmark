#!/bin/bash

export MPIR_CVAR_BCAST_INTRA_ALGORITHM=binomial
echo $MPIR_CVAR_BCAST_INTRA_ALGORITHM

#SBATCH --job-name=MPIbenchmark
#SBATCH --account=MPI
#SBATCH --partition=bdwall
#SBATCH --nodes=20
#SBATCH --output=MPIbenchmark.out
#SBATCH --error=MPIbenchmark.error
#SBATCH --time=01:00:00

for nodes in 1 4 8 16 20;
do
    for ppn in {1..36}
    do
        total_number_processes=`expr $nodes \* $ppn`
        mpiexec -n $total_number_processes -ppn $ppn ./test_normal_orientation
        mpiexec -n $total_number_processes -ppn $ppn ./test_orientation_shifted
        mpiexec -n $total_number_processes -ppn $ppn ./test_orientation_jumper
    done
done

