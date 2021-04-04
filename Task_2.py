#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 17:34:41 2021

@author: luca
"""


#This is the Task 2 example (fitted).

import numpy as np
import matplotlib.pyplot as plt

matX = np.array([[1, 1, 1], [0, 3, 6]])
matX =  matX.T #reshape this another way

matXT = matX.T

vecY = np.array([1, 4, 5])

matX_XT = matXT @ matX

matX_T_inv = np.linalg.inv(matX_XT) #The decimals in this are correct

matXT_vecY = matXT @ vecY

B = matX_T_inv @ matXT @ vecY #These decimals are correct

pred_vals = matX @ B #The fitted predicted values
#-------------

x_points = np.array([0, 3, 6])
y_points = np.array([1, 4, 5])

#y = np.array([1.33333333, 0.66666667, 2.66666667])

#You should plot the predicted values 
plt.scatter(x_points, y_points)
plt.grid()
plt.plot(x_points, pred_vals)
plt.show()


