# Advanced Meta-Learning Techniques: Prototypical Networks & MAML

##Overview
This repository contains my solutions to Problem Set 3 from Stanford's XCS330 course. The project focuses on two key meta-learning algorithms, Prototypical Networks (Protonets) and Model-Agnostic Meta-Learning (MAML), applied to few-shot image classification using the Omniglot dataset.

##Project Structure
src/:
protonet.py: Contains the implementation of Prototypical Networks.
maml.py: Contains the implementation of Model-Agnostic Meta-Learning (MAML).
protonet_results_*.npy: Results for Prototypical Networks experiments.
maml_results_*.npy: Results for MAML experiments.
submission.pdf: Detailed report covering the experimental results and analysis.

## Key Algorithms:
### 1. Prototypical Networks
Prototypical Networks classify images by computing class "prototypes" from support examples. Queries are classified based on their distance to these prototypes. The model demonstrated high accuracy, achieving strong generalization by learning robust representations.

### 2. Model-Agnostic Meta-Learning (MAML)
MAML is designed to find initial model parameters that can quickly adapt to new tasks with minimal data. I implemented both the inner and outer loops of MAML, testing the model's adaptability to new few-shot classification tasks, achieving high validation accuracy.

## Installation and Setup
To set up the project and run the experiments:

## Clone the Repository:

```bash
git clone https://github.com/TinaMoz/Meta-Learning-Protonets-MAML.git
```

## Install Dependencies:
```bash

pip install -r requirements.txt
```

## Running Protonet:
```bash

python protonet.py --num_support 5
```

##Running MAML:

```bash

python maml.py
```

## Results
Results from both Prototypical Networks and MAML experiments are saved in .npy files. Detailed analysis of the results can be found in submission.pdf.

## Tools & Technologies
- Python
- PyTorch
- Omniglot Dataset
- Google Colab (for GPU-accelerated training)

## Contributing
Contributions are welcome. Please fork the repository and submit a pull request with your improvements or suggestions.

## Honor Code Notice
This project contains coursework from Stanford University. Users and contributors are advised that all work submitted in this course is expected to be the result of individual effort and independent thinking. Collaboration or reference to past solutions from other students or sources is discouraged and should adhere to Stanford University's honor code. For more information, please visit Stanford's Community Standards.




