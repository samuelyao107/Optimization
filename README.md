# Optimization Algorithms

This repository contains implementations of various optimization algorithms. These algorithms are commonly used in mathematical optimization, artificial intelligence, and operations research to find the best solution from a set of possible solutions.

## Table of Contents
- [Overview](#overview)
- [Algorithms](#algorithms)
  - [Genetic Algorithm](#genetic-algorithm)
  - [Simulated Annealing](#simulated-annealing)
  - [Tabu Search](#tabu-search)
  - [Simple Descent Algorithm](#simple-descent-algorithm)
- [Installation](#installation)
- [Contributing](#contributing)


## Overview

This project provides Python implementations of several well-known optimization algorithms. Each algorithm aims to solve complex problems by searching for the most optimal solution, often within large and complex solution spaces.

## Algorithms

### Genetic Algorithm
The Genetic Algorithm is a heuristic search that mimics the process of natural selection. It is commonly used for solving optimization and search problems by evolving the best solution over several generations.

File: `Genetic_algorithm.py`

### Simulated Annealing
Simulated Annealing is a probabilistic technique for approximating the global optimum of a given function. It is useful when the search space is large, and other optimization techniques may get trapped in local optima.

File: `Simulated_Annealing.py`

### Tabu Search
Tabu Search is a metaheuristic search method that guides a local heuristic search procedure to explore the solution space beyond local optimality. It uses a tabu list to prevent cycling back to previously visited solutions.

File: `Tabu_Search.py`

### Simple Descent Algorithm
The Simple Descent Algorithm (also known as Gradient Descent) is an iterative optimization algorithm used to minimize a function by moving along the gradient's direction.

File: `Simple_Descent_Algorithm.py`

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/samuelyao107/Optimization.git
1. Ensure you have Python 3.x installed.
2. Install any required dependencies using pip.

## Contributing

Contributions are welcome! If you want to contribute:

1. Fork the repository.
2. Create a new feature branch:
   ```bash
   git checkout -b feature-branch
