import math
import numpy as np

######################################################################
# Calculates the Advantage based on the formula derived in Section 5
# specifically Subsection 5.5
# total_mixes: number of total mixes in the ACN
# corrupt_mixes: number of corrupt mixes in the ACN
######################################################################


def pr_advantage(total_mixes, corrupt_mixes):
    # If there is only one mix the advantage is always zero
    # independent if it is corrupted or not, since then
    # u_0 and u_1 will choose the same mix and thereby
    # it is always User Behavior B_5
    if total_mixes == 1:
        return 0
    return (1 - (math.comb(total_mixes-2, corrupt_mixes)/math.comb(total_mixes, corrupt_mixes))) * (1 - 1/total_mixes)**3 + (1 - math.comb(total_mixes-1, corrupt_mixes)/math.comb(total_mixes, corrupt_mixes))*2 * (1 - 1/total_mixes)**2 * 1/total_mixes


######################################################################
# Figure 9 : Advantage of the adversary depending
#            on the number of corrupted nodes for | M | = 1,000
######################################################################
def calculate_uniform_advantage_iterative(n):
    advantage = np.zeros(n+1)
    index = np.zeros(n+1)
    advantage[0] = pr_advantage(n, 1)
    index[0] = 1
    for i in range(2, len(advantage)):
        advantage[i-1] = pr_advantage(n, i)
        index[i-1] = i
    return index, advantage


ua_i_1k, ua_a_1k = calculate_uniform_advantage_iterative(1000)
np.savetxt('./lasthop_plot_all_1k.csv', np.column_stack((ua_i_1k, ua_a_1k)),
           header='indices,1k', comments='# ', delimiter=',', newline='\n')


######################################################################
# Figure 10 : Advantage of the adversary depending on the
#             proportion of the corrupted nodes.
#
# Combination of the previous data:
# - calculate_uniform_advantage_iterative(1000)
# and the last colum of this dataset:
# - calculate_advantage_big_steps(100000)
######################################################################
def calculate_advantage_steps(n, steps):
    advantage = np.zeros(steps)
    index = np.zeros(steps)
    step = int(n/steps)
    for i in range(1, len(advantage)+1):
        advantage[i-1] = pr_advantage(n, i*step)
        index[i-1] = step*i/n
    return index, advantage

# def calculate_advantage_percentage(n):
#    return calculate_advantage_steps(n, 100)


def calculate_advantage_big_steps(n):
    return calculate_advantage_steps(n, 5)


ratio = np.array([0.2, 0.4, 0.6, 0.8, 1])
_, advantage_1k_big_steps = calculate_advantage_big_steps(1000)
_, advantage_5k_big_steps = calculate_advantage_big_steps(5000)
_, advantage_10k_big_steps = calculate_advantage_big_steps(10000)
_, advantage_100k_big_steps = calculate_advantage_big_steps(100000)

np.savetxt('./lasthop_plot_ratio_big_steps.csv', np.column_stack((ratio, advantage_1k_big_steps, advantage_5k_big_steps,
           advantage_10k_big_steps, advantage_100k_big_steps)), header='big steps,1k,5k,10k,100k', comments='# ', delimiter=',', newline='\n')

######################################################################
# Figure 11 : Advantage of a global passive adversary depending
#             on the maximum fraction of users, a single mix can
#             serve as Last Hop.
######################################################################


def calculate_advantage_global_passive(m):
    advantage = np.zeros(m+1)
    index = np.zeros(m+1)
    advantage[0] = pr_advantage(1, 1)
    index[0] = 1
    for i in range(2, len(advantage)):
        advantage[i-1] = pr_advantage(i, i)
        index[i-1] = i
    return index, advantage


ua_i_full, ua_a_full = calculate_advantage_global_passive(10)

np.savetxt('./lasthop_plot_global_passive_10.csv', np.column_stack((ua_i_full, ua_a_full)),
           header='indices, advantage', comments='# ', delimiter=',', newline='\n')

######################################################################
# Figure 13 : Advantage of the adversary for uniform and
#             bandwidth-based cascade selection.
# Combined with the data from "calculate_bandwidth_advantage(5, 100)
######################################################################

i_proportions_1k, a_proportions_1k = calculate_advantage_steps(1000, 1000)

np.savetxt('./lasthop_plot_proportion_1k.csv', np.column_stack((i_proportions_1k, a_proportions_1k)),
           header='proportion, advantage', comments='# ', delimiter=',', newline='\n')
