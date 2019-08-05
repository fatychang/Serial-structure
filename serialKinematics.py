# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 11:16:03 2019

This script calculate the kinematics of the serial configuration based on the D-H convention


@author: jschang
"""

# Import
import numpy as np
import matplotlib.pyplot as plt



##### One link chain (one joint, i=1)
# D-H parameters
a_1 = 1
d_1 = 0
alpha_1 = 0
theta_1 = np.pi/4

# Transformation matrix from frame i to  frame (i-1)
A1 = np.matrix([[np.cos(theta_1), -np.sin(theta_1)*np.cos(alpha_1), np.sin(alpha_1)*np.sin(alpha_1), a_1 *np.cos(theta_1)],
                [np.sin(theta_1), np.cos(theta_1)*np.cos(alpha_1), -np.cos(theta_1)*np.sin(alpha_1), a_1*np.sin(theta_1)],
                [0, np.sin(alpha_1), np.cos(alpha_1), d_1 ],
                [0, 0, 0, 1]])

# Calculate the end-effector position
p1 = np.matrix([0, 0, 0, 1])
p1 = p1.transpose()
p2 = A1*p1


# Visualizae the result
x = np.array([p1.item(0), p2.item(0)])
y = np.array([p1.item(1), p2.item(1)])
plt.plot(x, y, 'o') #plot the joint and end-effector
plt.plot(x, y,'r') #plot the link
