#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 17:10:26 2021

@author: luca
"""
import numpy as np
import matplotlib.pyplot as plt


"""
#2-D Matrix Decomposition 1

M = np.array([[7,4],
              [4,5]])

#Check if Matrix is Symmetric
print('Check if Matrix is symmetric, M should be equal to its transpose: '
      , M == M.T, '\n')

#Get Eigenvectors and Values
V, P = np.linalg.eigh(M)
print('Eigenvalues: \n', V, '\n')
print('Eigenvectors: \n', P, '\n')


# Convert Eigenvectors to Diagonal Matrix
D = np.diag(V)
print('Diagonal Matrix: \n', D)

print('P = \n', P, '\n')
print('D = \n', D, '\n')
print('P x D x P^-1 = \n', P@D@np.linalg.inv(P), '\n')

print('Does P x D x P^-1 = M?\n')
print('Evaluating M with PDP^-1: \n', np.isclose(M, P@D@np.linalg.inv(P)))
"""
"""
#2-D Matrix Decomposition 2

M = np.array([[-6, 3], 
              [3, 4]])

#Check if Matrix is Symmetric
print('Check if Matrix is symmetric, M should be equal to its transpose: '
      , M == M.T, '\n')

#Get Eigenvectors and Values
V, P = np.linalg.eigh(M)
print('Eigenvalues: \n', V, '\n')
print('Eigenvectors: \n', P, '\n')


# Convert Eigenvectors to Diagonal Matrix
D = np.diag(V)
print('Diagonal Matrix: \n', D)

print('P = \n', P, '\n')
print('D = \n', D, '\n')
print('P x D x P^-1 = \n', P@D@np.linalg.inv(P), '\n')

print('Does P x D x P^-1 = M?\n')
print('Evaluating M with PDP^-1: \n', np.isclose(M, P@D@np.linalg.inv(P)))
"""

"""
# 3-D Matrix Decomposition 1

M = np.array([[6, 4, 4], 
              [4, 5, 5], 
              [4, 5, 5]])

#Check if Matrix is Symmetric
print('Check if Matrix is symmetric, M should be equal to its transpose: '
      , M == M.T, '\n')

#Get Eigenvectors and Values
V, P = np.linalg.eigh(M)
print('Eigenvalues: \n', V, '\n')
print('Eigenvectors: \n', P, '\n')


# Convert Eigenvectors to Diagonal Matrix
D = np.diag(V)
print('Diagonal Matrix: \n', D)

print('P = \n', P, '\n')
print('D = \n', D, '\n')
print('P x D x P^-1 = \n', P@D@np.linalg.inv(P), '\n')

print('Does P x D x P^-1 = M?\n')
print('Evaluating M with PDP^-1: \n', np.isclose(M, P@D@np.linalg.inv(P)))
"""

"""
# 3-D Matrix Decomposition 2

M = np.array([[1, -6, -6], 
              [-6, 4 ,4], 
              [-6, 4, 0]])

#Check if Matrix is Symmetric
print('Check if Matrix is symmetric, M should be equal to its transpose: '
      , M == M.T, '\n')

#Get Eigenvectors and Values
V, P = np.linalg.eigh(M)
print('Eigenvalues: \n', V, '\n')
print('Eigenvectors: \n', P, '\n')


# Convert Eigenvectors to Diagonal Matrix
D = np.diag(V)
print('Diagonal Matrix: \n', D)

print('P = \n', P, '\n')
print('D = \n', D, '\n')
print('P x D x P^-1 = \n', P@D@np.linalg.inv(P), '\n')

print('Does P x D x P^-1 = M?\n')
print('Evaluating M with PDP^-1: \n', np.isclose(M, P@D@np.linalg.inv(P)))
"""