# set up imports, not all are used
import numpy as np
import math
import time
import sys


if (len(sys.argv) < 7):
    print("You did not input enough cmd line arguments, expected: N, PPN, alpha1, alpha2, beta1, beta2")
    exit()

# hierarchical runtime formula
def calculate_time_hierarchical(B_inter, B_intra, a_inter, a_intra, m, N, PPN):
    return math.ceil(math.log2(N))*(B_inter * m + a_inter) + math.ceil(math.log2(PPN))*(B_intra * m + a_intra)


# setting up global vars

N = int(sys.argv[1]) # Number of Nodes
PPN = int(sys.argv[2]) # Processes Per Node
NP = PPN * N # Total Processes
alpha1 = float(sys.argv[3]) # Intranode latency
alpha2 = float(sys.argv[4]) # Internode latency
betan1 = float(sys.argv[5]) # Intranode bandwidth
betan2 = float(sys.argv[6])# Internode bandwidth

sends = []
recvs = []
times = [0.0 for i in range(NP)]
final_time = 0.0

# populates the list

def populate(rank, sends, recvs):
    mask = 0x1
    while (mask < NP):
        if (not(rank & mask == 0)):
            src = (rank - mask + NP) % NP
            recvs.append({"src":src})
            break
        mask <<= 1
    mask >>= 1
    while (mask > 0):
        if (rank + mask < NP):
            dst = (rank + mask) % NP
            sends.append({"dst":dst})
        mask >>= 1

def get_alpha_beta(src, dst):
    src_id = src // PPN
    dst_id = dst // PPN
    if (src_id == dst_id): # checks if they are on the same node
        return (alpha1 + betan1) / 2, 0
    else:
        return (alpha2 + betan2) / 2, 0

def update_message(src, dst, time):
    for t in recvs[dst]:
        if (t["src"] == src):
            t["time"] = time # mark the time that the process received the inf
            break

def progress(rank, sends, recvs):
    global final_time
    # print(times)
    while recvs: # while recvs is not empty
        if "time" in recvs[0]:
            copy, link = get_alpha_beta(recvs[0]["src"], rank)
            if (times[rank] < recvs[0]["time"]):
                # print("ENTERED HERE")
                # print(times[rank], " vs. ", recvs[0]["time"])
                times[rank] = recvs[0]["time"]
            times[rank] += copy
            recvs.pop(0)
            # print("POPPED", rank)
        else:
            break
    if (not recvs):
        for t in sends:
            copy, link = get_alpha_beta(rank, t["dst"])
            times[rank] += copy # add the copy time
            # we add the link time here which represents time spent traveling network, in this case the link time is always 0
            update_message(rank, t["dst"], times[rank] + link)
        if (final_time < times[rank]):
            final_time = times[rank]
        return 1 # return 1 indicating we finished one process's sends
    return 0

for i in range(NP):
    sends.append([])
    recvs.append([])
    populate(i, sends[i], recvs[i])
    ...
# call show_sends_recv
# call simulate
# dump final_time

n_complete = 0
while (n_complete < NP):
    for i in range(NP):
        n_complete += progress(i, sends[i], recvs[i])

f = open("results_theory.txt", "a")
f.write(str(final_time) + " " + str(N) + " " + str(PPN) + " " + str(alpha1) + " " + str(alpha2) + " " + str(betan1) + " " + str(betan2) + "\n")
f.close()
print(final_time)