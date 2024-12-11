import math
import numpy as np


def bandwidth_advantage(bandwidth, k):
    return 2 * bandwidth - 4 * (bandwidth**2) * 1/k + 2 * (bandwidth**3) * (1/k)**2 - bandwidth*(bandwidth * (k-1)/k) * (1 - bandwidth*(1/k)) * (1 - (bandwidth * (1/k)))


def calculate_bandwidth_advantage(p, k):
    advantage = np.zeros(p)
    index = np.zeros(p)
    for i in range(1, len(advantage)+1):
        b = (1/p) * i
        advantage[i-1] = bandwidth_advantage(b, k)
        index[i-1] = b
    return index, advantage


######################################################################
# Figure 12 : Advantage of the adversary depending on the
#             proportion of the corrupted bandwidth for different k.
######################################################################
bwa_i, bwa_a_10 = calculate_bandwidth_advantage(1000, 10)
bwa_i, bwa_a_100 = calculate_bandwidth_advantage(1000, 100)
bwa_i, bwa_a_1k = calculate_bandwidth_advantage(1000, 1000)

np.savetxt('./lasthop_plot_bandwidth.csv', np.column_stack((bwa_i, bwa_a_10, bwa_a_100, bwa_a_1k)),
           header='bandwidth_advantage,10,100,1k', comments='# ', delimiter=',', newline='\n')

bwa_i_big_steps, bwa_a_big_steps_1k = calculate_bandwidth_advantage(5, 1000)

np.savetxt('./lasthop_plot_bandwidth_big_steps_1k.csv', np.column_stack((bwa_i_big_steps,
           bwa_a_big_steps_1k)), header='bandwidth_advantage,1k', comments='# ', delimiter=',', newline='\n')


######################################################################
# Figure 13 : Advantage of the adversary for uniform and
#             bandwidth-based cascade selection.
######################################################################
bwa_i_big_steps, bwa_a_big_steps_100 = calculate_bandwidth_advantage(5, 100)

np.savetxt('./lasthop_plot_bandwidth_big_steps_100.csv', np.column_stack((bwa_i_big_steps,
           bwa_a_big_steps_100)), header='bandwidth_advantage,1k', comments='# ', delimiter=',', newline='\n')
