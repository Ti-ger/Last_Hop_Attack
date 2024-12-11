# The Last Hop Attack: Why Loop Cover Traffic over Fixed Cascades Threatens Anonymity
Paper and Code for the Last Hop Attack

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
git clone git@my_awesome_artifact.com/repo
apt install libxxx xxx
```
Describe the expected results where it makes sense to do so.

### Testing the Environment (Only for Functional and Reproduced badges)
Describe the basic functionality tests to check if the environment is set up correctly.
These tests could be unit tests, training an ML model on very low training data, etc..
If these tests succeed, all required software should be functioning correctly.
Include the expected output for unambiguous outputs of tests.
Use code segments to simplify the workflow, e.g.,
```bash
python envtest.py
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
Describe which tables and results are included or are not reproducible with the provided artifact.
Provide an argument why this is not included/possible.

## Notes on Reusability (Only for Functional and Reproduced badges)
First, this section might not apply to your artifacts.
Use it to share information on how your artifact can be used beyond your research paper, e.g., as a general framework.
The overall goal of artifact evaluation is not only to reproduce and verify your research but also to help other researchers to re-use and improve on your artifacts.
Please describe how your artifacts can be adapted to other settings, e.g., more input dimensions, other datasets, and other behavior, through replacing individual modules and functionality or running more iterations of a specific part.
