#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 17:34:41 2021

@author: luca
"""


#This is the Task 2 example (fitted).

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

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

x_axis = np.arange(start = 0, stop = 6.5, step = 1)
y_axis = np.arange(start = 0, stop = 6.5, step = 1)

x = np.arange(start = 0, stop = 3, step = 1)

x_variables = np.array([0, 3, 6]) #This controls the length of the x-axis (should be used for independent variables)
y_variables = np.array([1, 4, 5]) #This controls the length of the y-axis (should be used for dependent varibles)

#residuals = y_points - (x_points + y_points * x)

#y = np.array([1.33333333, 0.66666667, 2.66666667])

#You should plot the predicted values 
ax = plt.subplot()
ax.scatter(x_variables, y_variables)
ax.grid()
ax.plot(x_variables, pred_vals)
#plt.sm.graphics.plot()
plt.show()



plt.show()
