import os
import matplotlib.pyplot as plt
from pylab import *
norm = open("/scratch/test-mpi-build/bcast_benchmark/results.txt")
random = open("/scratch/test-mpi-build/bcast_benchmark/results_random.txt")
shift = open("/scratch/test-mpi-build/bcast_benchmark/results_shifted.txt")

norm_hier = open("/scratch/test-mpi-build/bcast_benchmark/results_hier.txt")
random_hier = open("/scratch/test-mpi-build/bcast_benchmark/results_hier_random.txt")
shift_hier = open("/scratch/test-mpi-build/bcast_benchmark/results_hier_shifted.txt")

x_axis = [j for j in range(1, 37)]

y_theory = []
y_norm = []
y_random = []
y_shift = []

y_hier_norm = []
y_hier_random = []
y_hier_shift = []
y_hier_theory = []

# clean up simulator outputs
# cleaner = open("/scratch/test-mpi-build/bcast_benchmark/results_theory.txt", "w")
# cleaner.write("")
# os.system("clear")
# cleaner.close()
# cleaner = open("/scratch/test-mpi-build/bcast_benchmark/results_hier_theory.txt", "w")
# cleaner.write("")
# os.system("clear")
# cleaner.close()

# latency_intra = "0.22"
# latency_inter = "0.45"

# for nodes in {1, 4, 8, 16, 20}:
#     for ppn in range(1, 37):
#         command = "python3 binomial_simulator.py " + str(nodes) + " " + str(ppn) + " " + "{} ".format(latency_intra) + "{} ".format(latency_inter) + "0 " + "0"
#         command_hier = "python3 hierarchical_simulator.py " + str(nodes) + " " + str(ppn) + " " + "{} ".format(latency_intra) + "{} ".format(latency_inter) + "0 " + "0"
#         os.system(command)
#         os.system(command_hier)

theory = open("/scratch/test-mpi-build/bcast_benchmark/results_theory.txt")
theory_hier = open("/scratch/test-mpi-build/bcast_benchmark/results_hier_theory.txt")

# Data parsing

for line in theory_hier:
    y_hier_theory.append(float(line.split()[0]))

for line in theory:
    y_theory.append(float(line.split()[0]))

for line in norm:
    y_norm.append(float(line.split()[0]))

for line in norm_hier:
    y_hier_norm.append(float(line.split()[0]))

for line in random:
    y_random.append(float(line.split()[0]))

for line in random_hier:
    y_hier_random.append(float(line.split()[0]))

for line in shift:
    y_shift.append(float(line.split()[0]))

for line in shift_hier:
    y_hier_shift.append(float(line.split()[0]))



y_theory_1_node = y_theory[0:36]
y_theory_4_node = y_theory[36:72]
y_theory_8_node = y_theory[72:108]
y_theory_16_node = y_theory[108:144]
y_theory_20_node = y_theory[144:180]

y_norm_1_node = y_norm[0:36]
y_norm_4_node = y_norm[36:72]
y_norm_8_node = y_norm[72:108]
y_norm_16_node = y_norm[108:144]
y_norm_20_node = y_norm[144:180]

y_random_1_node = y_random[0:36]
y_random_4_node = y_random[36:72]
y_random_8_node = y_random[72:108]
y_random_16_node = y_random[108:144]
y_random_20_node = y_random[144:180]

y_shift_1_node = y_shift[0:36]
y_shift_4_node = y_shift[36:72]
y_shift_8_node = y_shift[72:108]
y_shift_16_node = y_shift[108:144]
y_shift_20_node = y_shift[144:180]

y_hier_theory_1_node = y_hier_theory[0:36]
y_hier_theory_4_node = y_hier_theory[36:72]
y_hier_theory_8_node = y_hier_theory[72:108]
y_hier_theory_16_node = y_hier_theory[108:144]
y_hier_theory_20_node = y_hier_theory[144:180]

y_hier_norm_1_node = y_hier_norm[0:36]
y_hier_norm_4_node = y_hier_norm[36:72]
y_hier_norm_8_node = y_hier_norm[72:108]
y_hier_norm_16_node = y_hier_norm[108:144]
y_hier_norm_20_node = y_hier_norm[144:180]

y_hier_random_1_node = y_hier_random[0:36]
y_hier_random_4_node = y_hier_random[36:72]
y_hier_random_8_node = y_hier_random[72:108]
y_hier_random_16_node = y_hier_random[108:144]
y_hier_random_20_node = y_hier_random[144:180]

y_hier_shift_1_node = y_hier_shift[0:36]
y_hier_shift_4_node = y_hier_shift[36:72]
y_hier_shift_8_node = y_hier_shift[72:108]
y_hier_shift_16_node = y_hier_shift[108:144]
y_hier_shift_20_node = y_hier_shift[144:180]


plt.title("Runtime vs. PPN \n (1 Node, latency_intra = 0.22 μs, latency_inter = 0.45 μs)")
plt.xlabel("PPN (Processes Per Node)")
plt.ylabel("Time (μs)")
plt.plot(x_axis, y_norm_1_node, label="Flat")
plt.plot(x_axis, y_hier_norm_1_node, label="Topology-Aware")
plt.legend()
plt.grid()
plt.savefig("plot_1_node.png")
plot_1_node = plt.show()

plt.title("Runtime vs. PPN \n (4 Nodes, latency_intra = 0.22 μs, latency_inter = 0.45 μs)")
plt.xlabel("PPN (Processes Per Node)")
plt.ylabel("Time (μs)")
plt.plot(x_axis, y_norm_4_node, label="Flat")
plt.plot(x_axis, y_hier_norm_4_node, label="Topology-Aware")
plt.legend()
plt.grid()
plt.savefig("plot_4_node.png")
plot_4_node = plt.show()

plt.title("Runtime vs. PPN \n (8 Nodes, latency_intra = 0.22 μs, latency_inter = 0.45 μs)")
plt.xlabel("PPN (Processes Per Node)")
plt.ylabel("Time (μs)")
plt.plot(x_axis, y_norm_8_node, label="Flat")
plt.plot(x_axis, y_hier_norm_8_node, label="Topology-Aware")
plt.legend()
plt.grid()
plt.savefig("plot_8_node.png")
plot_8_node = plt.show()

plt.title("Runtime vs. PPN \n (16 Nodes, latency_intra = 0.22 μs, latency_inter = 0.45 μs)")
plt.xlabel("PPN (Processes Per Node)")
plt.ylabel("Time (μs)")
plt.plot(x_axis, y_norm_16_node, label="Flat")
plt.plot(x_axis, y_hier_norm_16_node, label="Topology-Aware")
plt.legend()
plt.grid()
plt.savefig("plot_16_node.png")
plot_16_node = plt.show()


rc('axes', linewidth=2)
ax = gca()


plt.title("Runtime vs. PPN \n (20 Nodes, latency_intra = 0.22 μs, latency_inter = 0.45 μs)", fontweight='bold')
plt.xlabel("PPN (Processes Per Node)", fontweight='bold')
plt.ylabel("Time (μs)", fontweight='bold')
plt.plot(x_axis, y_norm_20_node, label="Flat", linewidth=2)
plt.plot(x_axis, y_hier_norm_20_node, label="Topology-Aware", linewidth=2)
plt.legend()
plt.grid()

for tick in ax.xaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for tick in ax.yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')

plt.savefig("plot_20_node.png")
plot_20_node = plt.show()

rc('axes', linewidth=2)
ax = gca()

plt.title("Runtime vs. PPN \n (20 Nodes, latency_intra = 0.22 μs, latency_inter = 0.45 μs)", fontweight='bold')
plt.xlabel("PPN (Processes Per Node)", fontweight='bold')
plt.ylabel("Time (μs)",fontweight='bold')
plt.plot(x_axis, y_theory_20_node, label="Flat", linewidth=2)
plt.plot(x_axis, y_hier_theory_20_node, label="Topology-Aware", linewidth=2)
plt.grid()

for tick in ax.xaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for tick in ax.yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')

plt.legend()
plt.savefig("plot_theory_20_node.png")
plot_theory_20_node = plt.show()
# close fileopeners

norm.close()
random.close()
shift.close()
theory.close()

norm_hier.close()
random_hier.close()
shift_hier.close()
theory_hier.close()