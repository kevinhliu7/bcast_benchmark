import os
import matplotlib.pyplot as plt


norm = open("/scratch/test-mpi-build/bcast_benchmark/results.txt")
jump = open("/scratch/test-mpi-build/bcast_benchmark/results_jump.txt")
shift = open("/scratch/test-mpi-build/bcast_benchmark/results_shifted.txt")

x_axis = [j for j in range(1, 37)]

y_norm = []
y_jump = []
y_shift = []

for line in norm:
    y_norm.append(float(line))

for line in jump:
    y_jump.append(float(line))

for line in shift:
    y_shift.append(float(line))


y_norm_1_node = y_norm[0:36]
y_norm_4_node = y_norm[36:72]
y_norm_8_node = y_norm[72:108]
y_norm_16_node = y_norm[108:144]
y_norm_20_node = y_norm[144:180]

y_jump_1_node = y_jump[0:36]
y_jump_4_node = y_jump[36:72]
y_jump_8_node = y_jump[72:108]
y_jump_16_node = y_jump[108:144]
y_jump_20_node = y_jump[144:180]

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
plt.plot(x_axis, y_norm_1_node, label="Normal Orientation")
plt.plot(x_axis, y_shift_1_node, label="Shifted")
plt.plot(x_axis, y_jump_1_node, label="Modulus Distribution")
plt.legend()
plot_1_node = plt.show()
plt.savefig("plot_1_node.png")


plt.title("Runtime vs. PPN (4 Nodes)")
plt.xlabel("PPN")
plt.ylabel("Time (Microseconds)")
plt.plot(x_axis, y_norm_4_node, label="Normal Orientation")
plt.plot(x_axis, y_shift_4_node, label="Shifted")
plt.plot(x_axis, y_jump_4_node, label="Modulus Distribution")
plt.legend()
plot_4_node = plt.show()
plt.savefig("plot_4_node.png")


plt.title("Runtime vs. PPN (8 Nodes)")
plt.xlabel("PPN")
plt.ylabel("Time (Microseconds)")
plt.plot(x_axis, y_norm_8_node, label="Normal Orientation")
plt.plot(x_axis, y_shift_8_node, label="Shifted")
plt.plot(x_axis, y_jump_8_node, label="Modulus Distribution")
plt.legend()
plot_8_node = plt.show()
plt.savefig("plot_8_node.png")



plt.title("Runtime vs. PPN (16 Nodes)")
plt.xlabel("PPN")
plt.ylabel("Time (Microseconds)")
plt.plot(x_axis, y_norm_16_node, label="Normal Orientation")
plt.plot(x_axis, y_shift_16_node, label="Shifted")
plt.plot(x_axis, y_jump_16_node, label="Modulus Distribution")
plt.legend()
plot_16_node = plt.show()
plt.savefig("plot_16_node.png")


plt.title("Runtime vs. PPN (20 Nodes)")
plt.xlabel("PPN")
plt.ylabel("Time (Microseconds)")
plt.plot(x_axis, y_norm_20_node, label="Normal Orientation")
plt.plot(x_axis, y_shift_20_node, label="Shifted")
plt.plot(x_axis, y_jump_20_node, label="Modulus Distribution")
plt.legend()
plot_20_node = plt.show()
plt.savefig("plot_20_node.png")




norm.close()
jump.close()
shift.close()
    