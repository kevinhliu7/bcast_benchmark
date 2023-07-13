#!/bin/bash
#SBATCH --job-name=LatencyTest
#SBATCH --account=MPI
#SBATCH --partition=bdwall
#SBATCH --nodes=2
#SBATCH --output=latency.out
#SBATCH --error=latency.error
#SBATCH --time=00:20:00
for iterations in {1..50}
do
    mpiexec -n 2 -ppn 1 ./test_latency # internode
    mpiexec -n 2 -ppn 2 ./test_latency # intranode
done