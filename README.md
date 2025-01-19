# MNIST Image Classification

## 1. Project Overview


The MNIST project is a cornerstone in the machine learning community, approached here with my unique perspective.

The task is to classify grayscale images of handwritten digits, each sized 28x28 pixels, into one of 10 categories, representing the digits 0 through 9.

## 2. Project Workflow

### 2.1 Data Preparation:

**Dataset Partioning:** A set of 60,000 training images, plus 10,000 test images, assembled by the National Institute of Standards and Technology (the NIST in MNIST) in the 1980s. 

**Preprocessing:** Labels (originally digits from 0 to 9) are converted into a format called **one-hot vectors** before being fed into the neural network because using the original digits directly could mislead the neural network.

- The original digits (e.g., 0, 1, 2, ...) are numeric values, and the neural network might mistakenly treat them as having an inherent order or magnitude.

- For example, the model could assume that 9 is "larger" or "more important" than 0, which is incorrect since the digits represent distinct classes, not quantities.

### 2.2 Model Development:

Build a simple deep learning model with multiple hidden layers, ensuring no dropout is applied except in the final layer. Use the following configuration:
- Optimizer: adam for efficient optimization through adaptive learning rates

- Loss Function: `categorical_crossentropy` to measure the performance of the model in handling multi-class classification.

- Metrics: `accuracy` to track the proportion of correctly classified samples during training and evaluation.

- Activation Function: A `sigmoid` activation in the last layer to output probabilities for each digit class.

Optimized hyperparametes using Keras Tuner

## 3. Evaluation:

- Evaluated models on unseen data
  
