import os
import matplotlib.pyplot as plt


norm = open("/scratch/test-mpi-build/bcast_benchmark/results_hier.txt")
random = open("/scratch/test-mpi-build/bcast_benchmark/results_hier_random.txt")
shift = open("/scratch/test-mpi-build/bcast_benchmark/results_hier_shifted.txt")

x_axis = [j for j in range(1, 37)]

y_theory = []


y_norm = []
y_random = []
y_shift = []

cleaner = open("/scratch/test-mpi-build/bcast_benchmark/results_theory.txt", "w")
cleaner.write("")
os.system("clear")
cleaner.close()

for nodes in {1, 4, 8, 16, 20}:
    for ppn in range(1, 37):
        command = "python3 hierarchical_simulator.py " + str(nodes) + " " + str(ppn) + " " + "1.2 " + "1.4 " + "0 " + "0"
        os.system(command)
theory = open("/scratch/test-mpi-build/bcast_benchmark/results_theory.txt")

for line in theory:
    y_theory.append(float(line.split()[0]))

for line in norm:
    y_norm.append(float(line))

for line in random:
    y_random.append(float(line))

for line in shift:
    y_shift.append(float(line))

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

# print(y_norm_1_node)
# print(y_norm_4_node)
# print(y_norm_8_node)
# print(y_norm_16_node)
# print(y_norm_20_node)

plt.title("Runtime vs. PPN (1 Node)")
plt.xlabel("PPN")
plt.ylabel("Time (Microseconds)")
plt.plot(x_axis, y_theory_1_node, label="Theoretical")
plt.plot(x_axis, y_norm_1_node, label="Normal Orientation")
plt.plot(x_axis, y_shift_1_node, label="Shifted")
plt.plot(x_axis, y_random_1_node, label="Random Distribution")
plt.legend()
plt.savefig("plot_1_node.png")
plot_1_node = plt.show()

plt.title("Runtime vs. PPN (4 Nodes)")
plt.xlabel("PPN")
plt.ylabel("Time (Microseconds)")
plt.plot(x_axis, y_theory_4_node, label="Theoretical")
plt.plot(x_axis, y_norm_4_node, label="Normal Orientation")
plt.plot(x_axis, y_shift_4_node, label="Shifted")
plt.plot(x_axis, y_random_4_node, label="Random Distribution")
plt.legend()
plt.savefig("plot_4_node.png")
plot_4_node = plt.show()

plt.title("Runtime vs. PPN (8 Nodes)")
plt.xlabel("PPN")
plt.ylabel("Time (Microseconds)")
plt.plot(x_axis, y_theory_8_node, label="Theoretical")
plt.plot(x_axis, y_norm_8_node, label="Normal Orientation")
plt.plot(x_axis, y_shift_8_node, label="Shifted")
plt.plot(x_axis, y_random_8_node, label="Random Distribution")
plt.legend()
plt.savefig("plot_8_node.png")
plot_8_node = plt.show()

plt.title("Runtime vs. PPN (16 Nodes)")
plt.xlabel("PPN")
plt.ylabel("Time (Microseconds)")
plt.plot(x_axis, y_theory_16_node, label="Theoretical")
plt.plot(x_axis, y_norm_16_node, label="Normal Orientation")
plt.plot(x_axis, y_shift_16_node, label="Shifted")
plt.plot(x_axis, y_random_16_node, label="Random Distribution")
plt.legend()
plt.savefig("plot_16_node.png")
plot_16_node = plt.show()

plt.title("Runtime vs. PPN (20 Nodes)")
plt.xlabel("PPN")
plt.ylabel("Time (Microseconds)")
plt.plot(x_axis, y_theory_20_node, label="Theoretical")
plt.plot(x_axis, y_norm_20_node, label="Normal Orientation")
plt.plot(x_axis, y_shift_20_node, label="Shifted")
plt.plot(x_axis, y_random_20_node, label="Random Distribution")
plt.legend()
plt.savefig("plot_20_node.png")
plot_20_node = plt.show()

norm.close()
random.close()
shift.close()
theory.close()