#!/bin/bash
#SBATCH --job-name=LatencyTest
#SBATCH --account=MPI
#SBATCH --partition=bdwall
#SBATCH --nodes=2
#SBATCH --output=LatencyTest.out
#SBATCH --error=LatencyTest.error
#SBATCH --time=00:20:00

mpiexec -n 2 -ppn 1 ./test_internode
mpiexec -n 2 -ppn 2 ./test_intranode