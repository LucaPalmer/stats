#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 15:20:40 2021

@author: luca
"""
import numpy as np
import pandas as pd
import scipy.stats as stats
#from scipy.spatial import distance
import matplotlib.pyplot as plt


x = 1

mu = np.array([3, 6])

#Melbourne Housing Prices Taken from Kaggle

array1 = [1480000,  1035000, 1465000, 850000, 1600000, 941000, 1876000, 1636000,
300000, 1097000, 700000, 1350000, 750000, 1172500, 441000, 1310000, 1200000,
1176500, 955000 ]
array2  = [ 890000, 1330000, 900000, 1090000, 500000, 1100000, 1315000, 426000,
1447500, 457000, 1135000, 1542000, 1290000, 1290000, 470000, 1180000, 1195000,
1012500, 1030000]

print("\nArray 1: ", array1, "\n")
print("Array 2: ", array2, "\n")

cov = np.cov(array1, array2)

print("Covariance Matrix of Row Vectors = ", cov) # show covariance

print("\nCovariance Matrix Dimension: ", cov.ndim)

scalar = np.array([(x - mu.T)@np.linalg.inv(cov)@(x - mu)])


print("\n(x - m^T) * E^-1 * (x - m) = ", scalar, '\n')
print('Matrix (Scalar) Dimension of Result: ', scalar.ndim)


#2-D Contour plots

#------------
#Diagonalise the covariance matrix:

#Check if Matrix is Symmetric
print('Check if Covariance Matrix is symmetric, cov should be equal to its transpose: '
      , cov == cov.T, '\n')

#Get Eigenvectors and Values
V, P = np.linalg.eigh(cov)
print('Eigenvalues: \n', V, '\n')
print('Eigenvectors: \n', P, '\n')


# Convert Eigenvectors to Diagonal Matrix
D = np.diag(V)
print('Diagonal Matrix: \n', D)

print('P = \n', P, '\n')
print('D = \n', D, '\n')
print('P x D x P^-1 = \n', P@D@np.linalg.inv(P), '\n')

print('Does P x D x P^-1 = E?\n')
print('Evaluating E with PDP^-1: \n', np.isclose(cov, P@D@np.linalg.inv(P)))


a = 0.7
b = 1

#x = np.arange(0,210,0.125)
x = np.arange(-5 ,5, 0.1)
y = np.arange(-5, 5, 0.1)
stats.norm.pdf(x,loc=a,scale=b-a)

x, y = np.meshgrid(x, y)
z = x**2 + y**2

fig = plt.figure()
ax = fig.add_subplot()
ax.contour(x, y, z)
plt.show()

sample = np.random.normal(y)

"""
come back to this
x = np.linspace(0, 5, 100, endpoint = False)
y = stats.multivariate_normal.pdf(x, mean=2.5, cov=0.5)
"""