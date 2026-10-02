# Computational Intelligence – Assignments

This repository contains the implementations of two assignments developed for the **Computational Intelligence** course at the University of Ioannina.

The project focuses on two fundamental machine learning problems:

1. **Supervised Learning – Multilayer Perceptron (MLP)**
2. **Unsupervised Learning – K-Means Clustering**

The implementations were developed mainly in **C**.

---

# Assignment 1 – Multilayer Perceptron Classification

The first assignment focuses on the implementation and training of a **Multilayer Perceptron (MLP)** for a multiclass classification problem.

The dataset consists of two-dimensional input vectors:

```text
x = (x1, x2)
```

which belong to one of four classes:

```text
C1, C2, C3, C4
```

## Network Architecture

The MLP contains:

- 2 input neurons
- 3 hidden layers
- 4 output neurons

A configuration used during the experiments was:

```text
2 → 20 → 10 → 10 → 4
```

The implementation supports hidden-layer activation functions such as:

- Logistic / Sigmoid
- Hyperbolic Tangent (`tanh`)
- ReLU

For multiclass classification, the output layer uses **Softmax**.

---

## Training

Training is performed using:

- Forward propagation
- Backpropagation
- Gradient Descent
- Mini-batch weight updates
- Cross-entropy classification error

The weights and biases are initialized randomly and updated iteratively during training.

The program allows experimentation with parameters such as:

```text
Number of hidden neurons
Activation functions
Learning rate
Mini-batch size
Number of epochs
```

The goal is to study how the architecture and training parameters affect the classification performance of the network.

---

## Dataset

The main dataset files are:

```text
trainingData.csv
checkData.csv
```

Each example contains:

```text
x1, x2, class
```

The training dataset is used to train the neural network, while the test/check dataset is used to evaluate its classification ability on previously unseen examples.

---

## Output

After training, the program reports the classification results for the test dataset.

Each test example can be displayed as:

```text
+  -> correctly classified
-  -> incorrectly classified
```

The final classification accuracy is also calculated.

Because the initial weights are selected randomly, the exact result may vary between different executions.

---

# Assignment 2 – K-Means Clustering

The second assignment implements the **k-means clustering algorithm** for a two-dimensional dataset.

Unlike the first assignment, this is an **unsupervised learning** problem.

The objective is to divide the data into groups without using predefined class labels.

---

## K-Means Algorithm

For a selected number of clusters `M`, the algorithm starts by selecting `M` initial cluster centers.

The following steps are then repeated:

1. Compute the Euclidean distance of every point from all cluster centers.
2. Assign each point to the nearest center.
3. Recalculate every cluster center as the mean of the points assigned to it.
4. Repeat until the assignments no longer change.

The implementation follows this iterative procedure until convergence.

A maximum number of iterations is also used as a safety mechanism.

---

## Random Initialization

K-means is sensitive to the initial position of the cluster centers.

For this reason, for every value of `M`, the algorithm is executed:

```text
50 times
```

using different random initializations.

The initial centers are selected randomly from the dataset.

For every execution, the clustering error is calculated and the solution with the **minimum clustering error** is retained as the best solution.

The centers of the best solution are stored in output files such as:

```text
best_M*.txt
centers_M*.txt
```

---

## Number of Clusters

The algorithm was tested for:

```text
M = 3
M = 5
M = 7
M = 9
M = 11
M = 13
```

For every value of `M`, the data points and the centers of the best clustering solution were plotted.

The data points are represented with:

```text
+
```

while the cluster centers are represented with:

```text
X
```

For small values of `M`, multiple natural groups are merged into the same cluster.

For larger values of `M`, some natural groups are divided into multiple clusters.

For `M = 9`, the centers are positioned near the centers of the natural clusters of the dataset.

---

## Clustering Error

For every value of `M`, the minimum clustering error obtained from the 50 executions is stored.

An additional graph is created showing the clustering error as a function of the number of clusters:

```text
Clustering Error
       |
       |
       |
       +------------------> Number of clusters (M)
```

The clustering error decreases as the number of clusters increases.

However, the reduction is much more significant until:

```text
M = 9
```

After this point, increasing the number of clusters produces only a relatively small additional reduction in error.

This creates an **elbow point** in the error curve.

For the dataset used in this assignment, the elbow is observed at:

```text
M = 9
```

which also corresponds to the actual number of natural clusters in the dataset.

---

# Project Structure

An example structure of the repository is:

```text
Computational-Intelligence/
│
├── Assignment-1-MLP/
│   ├── mlp.c
│   ├── trainingData.csv
│   └── checkData.csv
│
├── Assignment-2-KMeans/
│   ├── ask2.c
│   ├── SDO.txt
│   ├── best_M*.txt
│   └── centers_M*.txt
│
└── README.md
```

---

# Compilation

## Assignment 1

Using GCC:

```bash
gcc mlp.c -o mlp -lm
```

Run:

```bash
./mlp
```

On Windows:

```bash
gcc mlp.c -o mlp.exe -lm
mlp.exe
```

---

## Assignment 2

Using GCC:

```bash
gcc ask2.c -o ask2 -lm
```

Run:

```bash
./ask2
```

On Windows:

```bash
gcc ask2.c -o ask2.exe -lm
ask2.exe
```

---

# Technologies

- C
- GCC
- Machine Learning
- Artificial Neural Networks
- Multilayer Perceptron
- Forward Propagation
- Backpropagation
- Gradient Descent
- Softmax Classification
- K-Means
- Clustering
- Euclidean Distance
- Data Visualization

---

# Results

## Assignment 1

The MLP is trained to solve a nonlinear multiclass classification problem.

Its performance depends on several parameters, including:

- Network architecture
- Number of hidden neurons
- Activation functions
- Learning rate
- Mini-batch size
- Number of training epochs
- Random initialization of weights

The trained network is evaluated using data that were not used during the training process.

---

## Assignment 2

The k-means experiments demonstrate the effect of the number of clusters on both the clustering error and the structure of the resulting groups.

For small values of `M`, natural clusters are merged.

For very large values of `M`, some natural clusters are divided into multiple groups.

The experiments indicate that:

```text
M = 9
```

provides a good representation of the natural structure of the dataset.

---

# Authors

- Nikolaos Skretas
- Emmanouil Georgios Emmanouilidis
---

# Course

**Computational Intelligence**  
**University of Ioannina**
