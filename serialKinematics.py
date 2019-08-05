# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 11:16:03 2019

This script calculate the kinematics of the serial configuration based on the D-H convention.
It contains the example from 1 joint to 3 joints.
The configuration of each joint and link will be displayed in the visualization plot.

@author: jschang
"""

# Import
import numpy as np
import matplotlib.pyplot as plt



##### One joint chain
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
ef = A1*p1


# Visualizae the result
x = np.array([p1.item(0), ef.item(0)])
y = np.array([p1.item(1), ef.item(1)])
plt.plot(x, y, 'o') #plot the joint and end-effector
plt.plot(x, y,'r') #plot the link
plt.title('One joint chain kinematic visualization')



##### two joints link chain
# D-H parameters
a = np.array([1,1])
d = np.array([0,0])
alpha = np.array([0,0])
theta = np.array([np.pi/4, np.pi/3])

# Modify the rotation angles
theta[1] = theta[1] - theta[0]

# Transformation matrix from frame i to  frame (i-1), stores in list A
A = list()
num_joints = 2
for i in range(num_joints):
    T = np.matrix([[np.cos(theta[i]), -np.sin(theta[i])*np.cos(alpha[i]), np.sin(alpha[i])*np.sin(alpha[i]), a[i] *np.cos(theta[i])],
                [np.sin(theta[i]), np.cos(theta[i])*np.cos(alpha[i]), -np.cos(theta[i])*np.sin(alpha[i]), a[i]*np.sin(theta[i])],
                [0, np.sin(alpha[i]), np.cos(alpha[i]), d[i]],
                [0, 0, 0, 1]])
    A.append(T)

# Calculate the end-effector position
p1 = np.matrix([0, 0, 0, 1])
p1 = p1.transpose()
p2 = A[0]* p1
ef = A[0] *A[1] *p1
    
# Visualizae the result
plt.figure()
x = np.array([p1.item(0), p2.item(0), ef.item(0)])
y = np.array([p1.item(1), p2.item(1), ef.item(1)])
plt.plot(x, y, 'o') #plot the joint and end-effector
plt.plot(x, y,'r') #plot the link
plt.title('Two joints chain kinematic visualization')


##### two joints link chain
# D-H parameters 
a = np.array([1,1,1])
d = np.array([0,0,0])
alpha = np.array([0,0,0])
theta = np.array([np.pi/4, np.pi/3, np.pi/4])

# Modify the rotation angles
theta[2] = theta[2] - theta[1]
theta[1] = theta[1] - theta[0]

# Transformation matrix from frame i to  frame (i-1), stores in list A
A = list()
num_joints = 3
for i in range(num_joints):
    T = np.matrix([[np.cos(theta[i]), -np.sin(theta[i])*np.cos(alpha[i]), np.sin(alpha[i])*np.sin(alpha[i]), a[i] *np.cos(theta[i])],
                [np.sin(theta[i]), np.cos(theta[i])*np.cos(alpha[i]), -np.cos(theta[i])*np.sin(alpha[i]), a[i]*np.sin(theta[i])],
                [0, np.sin(alpha[i]), np.cos(alpha[i]), d[i]],
                [0, 0, 0, 1]])
    A.append(T)

# Calculate the end-effector position
p1 = np.matrix([0, 0, 0, 1])
p1 = p1.transpose()
p2 = A[0]* p1
p3 = A[0] *A[1] *p1
ef = A[0] *A[1]* A[2] *p1
    
# Visualizae the result
plt.figure()
x = np.array([p1.item(0), p2.item(0), p3.item(0), ef.item(0)])
y = np.array([p1.item(1), p2.item(1), p3.item(1), ef.item(1)])
plt.plot(x, y, 'o') #plot the joint and end-effector
plt.plot(x, y,'r') #plot the link
plt.title('Three joints chain kinematic visualization')



