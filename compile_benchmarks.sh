#!/bin/bash

mpicc bcast_benchmark.c -o test_orientation_normal
mpicc bcast_benchmark_random.c -o test_orientation_random
mpicc bcast_benchmark_shifted.c -o test_orientation_shifted
mpicc latency_test.c -o test_latency