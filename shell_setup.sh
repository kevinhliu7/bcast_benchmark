#!/bin/bash

export MPIR_CVAR_BCAST_INTRA_ALGORITHM=binomial
echo $MPIR_CVAR_BCAST_INTRA_ALGORITHM

for nodes in {1..50}
do
    #SBATCH --job-name=<my_job_name>
    #SBATCH --account=<my_lcrc_project_name>
    #SBATCH --partition=bdwall
    #SBATCH --nodes=$nodes
    #SBATCH --ntasks-per-node=64
    #SBATCH --output=<my_job_name>.out
    #SBATCH --error=<my_job_name>.error
    #SBATCH --time=05:00:00
done

