# The Last Hop Attack: Why Loop Cover Traffic over Fixed Cascades Threatens Anonymity
Paper and Code for the Last Hop Attack

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
impossibility result is the first to show that loop cover traffic can
threaten anonymity. It allows us to conclude that mix nets that
utilize loop cover traffic and fixed cascades must deploy additional
cover traffic to achieve strong anonymity.

# Reproduce Results

## Docker
```
 docker build -t last_hop_attack .
 docker run -v "$(pwd)/data:/usr/src/app/data" last_hop_attack:latest
```

## Python
```
python lasthop_anonymity_sets.py; python lasthop_advantage_uniform_cascade_selection.py; python lasthop_advantage_bandwidth_based_cascade_selection.py
```

# Artifact Appendix

Paper title: **The Last Hop Attack: Why Loop Cover Traffic over Fixed
Cascades Threatens Anonymity**
Artifacts HotCRP Id: **https://artifact.petsymposium.org/artifact2025.2/paper.php/15** (not your paper Id, but the artifacts id)

Requested Badge: **Reproduced**

## Description
A main goal of this paper in general was reproducibility. This starts with our choice of the methodology, formal proofs and calculation and continues with the publication of the source code we used for these calculations. 

This artifact contains the code which was used in our paper. 
lasthop_anonymity_sets.py : Figure 2
lasthop_advantage_uniform_cascade_selection.py : Figures 9, 10, 11, 13
lasthop_advantage_bandwidth_based_cascade_selection.py : Figures 12, 13

### Security/Privacy Issues and Ethical Concerns (All badges)
There is no security, privacy, or ethical issue in using this artifact.

## Basic Requirements (Only for Functional and Reproduced badges)
This artifact requires Python3 and the libraries numpy and math

### Hardware Requirements
Any computer you can read this site on should suffice to run the scripts.

### Software Requirements
This artifact requires Python3 and the libraries numpy and math

### Estimated Time and Storage Consumption
The runs should not take longer than a minute and consume more than a few megabytes of storage

## Environment 
In the following, describe how to access our artifact and all related and necessary data and software components.
Afterward, describe how to set up everything and how to verify that everything is set up correctly.

### Accessibility (All badges)
Describe how to access your artifact via persistent sources.
Valid hosting options are institutional and third-party digital repositories.
Do not use personal web pages.
For repositories that evolve over time (e.g., Git Repositories ), specify a specific commit-id or tag to be evaluated.
In case your repository changes during the evaluation to address the reviewer's feedback, please provide an updated link (or commit-id / tag) in a comment.

### Set up the environment (Only for Functional and Reproduced badges)
Describe how the reviewers should set up the environment for your artifact, including downloading and installing dependencies and the installation of the artifact itself.
Be as specific as possible here.
If possible, use code segments to simply the workflow, e.g.,

```bash
git clone https://github.com/Ti-ger/Last_Hop_Attack.git
cd Last_Hop_Attack
docker build -t last_hop_attack .
docker run -v "$(pwd)/data:/usr/src/app/data" last_hop_attack:latest
```

You should find the recalculated data in the "data" directory

### Testing the Environment (Only for Functional and Reproduced badges)
A functional docker environment should suffice
```bash
docker run hello-world
```

## Artifact Evaluation (Only for Functional and Reproduced badges)
This section includes all the steps required to evaluate your artifact's functionality and validate your paper's key results and claims.
Therefore, highlight your paper's main results and claims in the first subsection. And describe the experiments that support your claims in the subsection after that.

### Main Results and Claims
List all your paper's results and claims that are supported by your submitted artifacts.

#### Main Result 1: Name
Describe the results in 1 to 3 sentences.
Refer to the related sections in your paper and reference the experiments that support this result/claim.

#### Main Result 2: Name
...

### Experiments 
List each experiment the reviewer has to execute. Describe:
 - How to execute it in detailed steps.
 - What the expected result is.
 - How long it takes and how much space it consumes on disk. (approximately)
 - Which claim and results does it support, and how.

#### Experiment 1: Name
Provide a short explanation of the experiment and expected results.
Describe thoroughly the steps to perform the experiment and to collect and organize the results as expected from your paper.
Use code segments to support the reviewers, e.g.,
```bash
python experiment_1.py
```
#### Experiment 2: Name
...

#### Experiment 3: Name 
...

## Limitations (Only for Functional and Reproduced badges)
All calculations done in the paper can be reproduced with this artifact

## Notes on Reusability (Only for Functional and Reproduced badges)
The code is focused on the Last Hop Attack and while it might serve as a pointer for further calculations a direct reusability was not intended
