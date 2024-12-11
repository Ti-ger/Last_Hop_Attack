import math
import numpy as np

######################################################################
# Figure 2 :  Size of the Receiver Anonymity Set,
# depending on the number of observed epochs and
# the number of users with | M | = 1, 000, 𝑥 = 5 and |𝐴| = 1.
######################################################################


def calculate_easi(mixes, users, comm, num_epochs):
    easis = np.zeros(num_epochs)
    inital_set = (1/mixes) * users * (comm + 1)
    prob_to_remain = (1.0-(1.0-(1/mixes))**(comm + 1))
    for epoch in range(num_epochs):
        easis[epoch] = inital_set * (prob_to_remain**epoch) + 1
    return easis


mixes = 1000
comm = 5
epochs = 3

easis_5000 = calculate_easi(mixes, 5000, comm, epochs)
easis_10000 = calculate_easi(mixes, 10000, comm, epochs)
easis_50000 = calculate_easi(mixes, 50000, comm, epochs)
easis_100000 = calculate_easi(mixes, 100000, comm, epochs)
easis_1000000 = calculate_easi(mixes, 1000000, comm, epochs)

index = np.arange(1, epochs+1)

np.savetxt('./easis.csv', np.column_stack((index, easis_5000, easis_10000, easis_50000,
           easis_100000, easis_1000000)), header='epoch,5k,10k,50k,100k,1M', comments='# ', delimiter=',', newline='\n')
