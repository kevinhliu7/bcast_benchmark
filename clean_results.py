import os

f = open("results.txt", "w")
f1 = open("results_random.txt", "w")
f2 = open("results_shifted.txt", "w")
f3 = open("results_hier.txt", "w")
f4 = open("results_hier_random.txt", "w")
f5 = open("results_hier_shifted.txt", "w")
f6 = open("results_hier_theory.txt", "w")
f7 = open("results_theory.txt", "w")

g = open("latency.txt", "w")

g.write("")

f6.write("")
f7.write("")
f2.write("")
f1.write("")
f.write("")
f3.write("")
f4.write("")
f5.write("")

f.close()
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()

g.close()