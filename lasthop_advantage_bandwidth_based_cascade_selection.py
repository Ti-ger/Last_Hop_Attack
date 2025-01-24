import math
import numpy as np
import os

######################################################################
#               Variables
######################################################################
output_directory = "data"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

######################################################################
# Calculates the Advantage based on the formula derived in Appendix C
# bandwidth_total       : total bandwidth in the network
# bandwidth_adversary   : bandwidth available to the adversary
# k                     : mixes available to the adversary
######################################################################


def bandwidth_advantage(bandwidth_total, bandwidth_adversary, k):
    bandwidth_ratio = bandwidth_adversary/bandwidth_total
    return 2 * bandwidth_ratio - 4 * (bandwidth_ratio**2) * 1/k + 2 * (bandwidth_ratio**3) * (1/k)**2 - bandwidth_ratio*(bandwidth_ratio * (k-1)/k) * (1 - bandwidth_ratio*(1/k)) * (1 - (bandwidth_ratio * (1/k)))


def calculate_bandwidth_advantage(bandwidth_total, k):
    advantage = np.zeros(bandwidth_total)
    index = np.zeros(bandwidth_total)
    for bandwidth_adversary in range(1, len(advantage)+1):
        advantage[bandwidth_adversary -
                  1] = bandwidth_advantage(bandwidth_total, bandwidth_adversary, k)
        index[bandwidth_adversary-1] = bandwidth_adversary
    return index, advantage


def calculate_bandwidth_advantage_big_steps(bandwidth_total, k, steps):
    advantage = np.zeros(steps)
    index = np.zeros(steps)
    bandwidth_share = bandwidth_total / steps
    for step in range(1, len(advantage)+1):
        bandwidth_adversary = bandwidth_share * step
        advantage[step -
                  1] = bandwidth_advantage(bandwidth_total, bandwidth_adversary, k)
        index[step-1] = bandwidth_adversary
    return index, advantage


######################################################################
# Figure 12 : Advantage of the adversary depending on the
#             proportion of the corrupted bandwidth for different k.
######################################################################
bwa_i, bwa_a_10 = calculate_bandwidth_advantage(1000, 10)
bwa_i, bwa_a_100 = calculate_bandwidth_advantage(1000, 100)
bwa_i, bwa_a_1k = calculate_bandwidth_advantage(1000, 1000)

np.savetxt(os.path.join(output_directory, './lasthop_plot_bandwidth.csv'), np.column_stack((bwa_i, bwa_a_10, bwa_a_100, bwa_a_1k)),
           header='bandwidth_advantage,10,100,1k', comments='# ', delimiter=',', newline='\n')

bwa_i_big_steps, bwa_a_big_steps_1k = calculate_bandwidth_advantage_big_steps(
    1000, 1000, 5)
np.savetxt(os.path.join(output_directory, './lasthop_plot_bandwidth_big_steps_1k.csv'), np.column_stack((bwa_i_big_steps,
           bwa_a_big_steps_1k)), header='bandwidth_advantage,1k', comments='# ', delimiter=',', newline='\n')


######################################################################
# Figure 13 : Advantage of the adversary for uniform and
#             bandwidth-based cascade selection.
# Combined with the data from "advantage_uniform_cascade_selection"
######################################################################
bwa_i_big_steps, bwa_a_big_steps_100 = calculate_bandwidth_advantage_big_steps(
    1, 100, 5)

np.savetxt(os.path.join(output_directory, './lasthop_plot_bandwidth_big_steps_100.csv'), np.column_stack((bwa_i_big_steps,
           bwa_a_big_steps_100)), header='bandwidth_advantage,100', comments='# ', delimiter=',', newline='\n')
