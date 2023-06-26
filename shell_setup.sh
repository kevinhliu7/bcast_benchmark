#!/bin/bash

export MPIR_CVAR_BCAST_INTRA_ALGORITHM=binomial
echo $MPIR_CVAR_BCAST_INTRA_ALGORITHM

#SBATCH --job-name=<my_job_name>
#SBATCH --account=MPI
#SBATCH --partition=bdwall
#SBATCH --nodes=20
#SBATCH --ntasks-per-node=64 # Can I get rid of this?
#SBATCH --output=<my_job_name>.out
#SBATCH --error=<my_job_name>.error
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

