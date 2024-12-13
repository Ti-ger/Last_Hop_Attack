# The Last Hop Attack: Why Loop Cover Traffic over Fixed Cascades Threatens Anonymity

# Abstract
Advanced mix net designs use a combination of loop cover traffic
and fixed cascades to detect when active adversaries delay or drop
messages. In this paper, we propose the Last Hop Attack, a new
attack algorithm that takes advantage of the fact that users send
loop cover, i.e., messages sent to themselves over the same mix
nodes that they also use to communicate with others. We use established privacy definitions based on indistinguishability games and
prove that our algorithm can break strong anonymity notions. Our
research shows that the Last Hop Attack breaks Sender Receiver
Pair Unlinkability for any Anonymous Communication Network
that utilizes loop cover traffic, fixed cascades, and no additional
cover traffic. We furthermore conclude that the notions of Sender
Message Unlinkability, Receiver Message Unlinkability (and Unobservability), and Both Side Unlinkability (and Unobservability)
are unachievable in this setting. To the best of our knowledge, this
impossibility result is the first to show that loop-cover traffic can
threaten anonymity. It allows us to conclude that mix nets that
utilize loop cover traffic and fixed cascades must deploy additional
cover traffic to achieve strong anonymity.

# Data

The data directory contains the calculation results. This repository contains all scripts needed to reproduce these results.

## Docker

### Load Docker Image
```
docker load < last_hop_attack.tar 
```

### Run Docker Image
```
docker run -v "$(pwd)/data:/usr/src/app/data" last_hop_attack:latest
```
### Rebuild Docker Container
```
 docker build -t last_hop_attack .
```

## Python
```
python lasthop_anonymity_sets.py; python lasthop_advantage_uniform_cascade_selection.py; python lasthop_advantage_bandwidth_based_cascade_selection.py
```

# Artifact Appendix

Paper title: **The Last Hop Attack: Why Loop Cover Traffic over Fixed
Cascades Threatens Anonymity**

Artifacts HotCRP Id: **https://artifact.petsymposium.org/artifact2025.2/paper.php/15**

Requested Badge: **Reproduced**

## Description
A primary goal of this paper, in general, was reproducibility. This starts with our choice of the methodology, formal proofs, and calculations and continues with the publication of the source code we used for these calculations. 

This artifact contains the code which was used in our paper. 
- lasthop_anonymity_sets.py : Figure 2
- lasthop_advantage_uniform_cascade_selection.py : Figures 9, 10, 11, 13
- lasthop_advantage_bandwidth_based_cascade_selection.py : Figures 12, 13

### Security/Privacy Issues and Ethical Concerns (All badges)
There is no security, privacy, or ethical issue in using this artifact.

## Basic Requirements (Only for Functional and Reproduced badges)
This artifact requires Python3 and the library numpy.

### Hardware Requirements
Any computer on which you can read this site should suffice to run the scripts.

### Software Requirements
This artifact requires Python3 and the library numpy.

### Estimated Time and Storage Consumption
The runs should not take longer than a minute and consume more than a few megabytes of storage.

## Environment 
In the following, we describe how to access our artifact and all related and necessary data and software components.
Afterward, we describe how to set up everything and how to verify that everything is set up correctly.

### Set up the environment
First, clone the repository to your computer.
```bash
git clone https://github.com/Ti-ger/Last_Hop_Attack.git
cd Last_Hop_Attack
```
Then, either execute the scripts with Python or use the provided Docker container. If you want, you can also build the Docker container yourself.
## Docker

### Load Docker Image
```
docker load < last_hop_attack.tar 
```

### Run Docker Image
```
docker run -v "$(pwd)/data:/usr/src/app/data" last_hop_attack:latest
```
### Rebuild Docker Container
```
 docker build -t last_hop_attack .
```

## Python
```
python lasthop_anonymity_sets.py; python lasthop_advantage_uniform_cascade_selection.py; python lasthop_advantage_bandwidth_based_cascade_selection.py
```

You should find the recalculated data in the "data" directory.

### Testing the Environment
A functional docker environment should suffice
```bash
docker run hello-world
```

## Artifact Evaluation

### Main Results and Claims


#### Main Result 1: The Receiver Anonymity Set quickly decays when multiple epochs are observed
See Section 2.4 Expected Anonymity Set Size, Section 2.5 Multiple Epochs, Figure 2 and [Experiment 1](#experiment-1-the-receiver-anonymity-set-quickly-decays-when-multiple-epochs-are-observed).

In certain situations, the adversary may be able to correlate their
observations across multiple epochs. In this case, the anonymity sets can be intersected
and quickly decay even if the initial number of users in the anonymity set is high (1.000.000).

#### Main Result 2: The Advantage of the Adversary is non-negligible for the global passive adversary and even for partially global adversaries
See Section 5 and Section 6, Figure 9 and Figure 10, and [Experiment 2](experiment-2-the-advantage-of-the-adversary-is-non-negligible-for-the-global-passive-adversary-and-even-for-partially-global-adversaries).

We show that the advantage for the global passive adversary converges to ≈ 0.999 and is thereby non-negligible; we furthermore argue that an adversary who has corrupted only a part of the network still has a non-negligible advantage but leave the choice at which exact point this is the case to the reader.

#### Main Result 3: The advantage of a global passive adversary is even for a low number of last hops non-negligible
See Section 7.1.2, Figure 11, and [Experiment 3](#main-result-3-the-advantage-of-a-global-passive-adversary-is-even-for-a-low-number-of-last-hops-non-negligible).

We show that even if only a small number of mixes (1 - 10) is used, the advantage of the adversary is still non-negligible.

#### Main Result 4: The advantage of a global passive adversary is also for a bandwidth-based cascade selection non-negligible
See Appendix C, Figure 12, Figure 13, and [Experiment 4](#main-result-4-the-advantage-of-a-global-passive-adversary-is-also-for-a-bandwidth-based-cascade-selection-non-negligible).

In our paper, we considered a uniform selection of the mixes in the cascade (𝐴4) and a uniform selection of corrupted mixes. We sketch that the Last Hop Attack is also viable when other types of cascade selection, e.g., bandwidth-based cascade selection, are used.

### Experiments 

#### Experiment 1: The Receiver Anonymity Set quickly decays when multiple epochs are observed
Script: lasthop_anonymity_sets.py

Data: 
- data/easis.csv

#### Experiment 2: The Advantage of the Adversary is non-negligible for the global passive adversary and even for partially global adversaries
Script: lasthop_advantage_uniform_cascade_selection.py 

Data: 
- data/lasthop_plot_all_1k.csv
- data/lasthop_plot_ratio_big_steps.csv

#### Experiment 3: The advantage of a global passive adversary is even for a low number of last hops non-negligible
Script: lasthop_advantage_uniform_cascade_selection.py 

Data: 
- data/lasthop_plot_global_passive_10.csv

#### Experiment 4: The advantage of a global passive adversary is also for a bandwidth-based cascade selection non-negligible 
Script: lasthop_advantage_bandwidth_based_cascade_selection.py

Data: 
- data/lasthop_plot_bandwidth.csv
- data/lasthop_plot_bandwidth_big_steps_1k.csv
- data/./lasthop_plot_bandwidth_big_steps_100.csv

## Limitations (Only for Functional and Reproduced badges)
All calculations done in the paper can be reproduced with this artifact.

## Notes on Reusability (Only for Functional and Reproduced badges)
The code is focused on the Last Hop Attack, and while it might serve as a pointer for further calculations, a direct reusability was not intended.
