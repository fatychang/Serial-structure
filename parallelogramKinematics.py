# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 13:13:52 2019

@author: jschang
"""

#import
import numpy as np
import matplotlib.pyplot as plt

############################################################################
# First configuration where the parallelogram is as described as below:
# 1. first two joints connect to the link 0 is link1' and link1''
# 2. joint 4 is selected as the cut joint
# 3. a1' = a3' and a2' = a1''
# End-effector is connected on joint 4 and all the params are all constant
#############################################################################

## Input
#input_theta1 = 2* np.pi/3
#input_theta2 = np.pi/3
#
#
## Constraints for close-loop chain based on this configuration
## this constraints is obtained by having the same position from two parts of the chains
#theta2 = input_theta2 - input_theta1
#theta3 = np.pi - theta2
#
## Obtain the first part of the chain (from link 0 - link1'-link2'-link3')
## DH params
#a = np.array([1,2,1])
#d = np.array([0,0,0])
#alpha = np.array([0,0,0])
#theta = np.array([input_theta1, theta2, theta3])
#
#
## Transformation matrix from frame i to  frame (i-1), stores in list A
#A = list()
#num_joints = 3
#for i in range(num_joints):
#    T = np.matrix([[np.cos(theta[i]), -np.sin(theta[i])*np.cos(alpha[i]), np.sin(alpha[i])*np.sin(alpha[i]), a[i] *np.cos(theta[i])],
#                [np.sin(theta[i]), np.cos(theta[i])*np.cos(alpha[i]), -np.cos(theta[i])*np.sin(alpha[i]), a[i]*np.sin(theta[i])],
#                [0, np.sin(alpha[i]), np.cos(alpha[i]), d[i]],
#                [0, 0, 0, 1]])
#    A.append(T)
#    
## Obtain the second part of the chain (from link 0 - link1'')
#a2=a[1]
#d2=0
#alpha2=0
#theta2=np.pi/4
#
## Transformation from link0 to link1''
#A2 = np.matrix([[np.cos(theta2), -np.sin(theta2), 0, a2*np.cos(theta2)],
#                [np.sin(theta2), np.cos(theta2), 0, a2*np.sin(theta2)],
#                [0,0,1,0],
#                [0,0,0,1]])
#
## Transformation from frame 3 to frame 4 (end-effector)
#a3 = 1
#A3 = np.matrix([[1, 0, 0, a3],
#                [0, 1, 0, 0],
#                [0, 0, 1, 0],
#                [0, 0, 0, 1]])
#    
#    
## Calculate the end-effector position and position of each joint
#p1 = np.matrix([0, 0, 0, 1])
#p1 = p1.transpose()
#p2 = A[0]* p1
#p3 = A[0] *A[1] *p1
#p4 = A[0] *A[1]* A[2] *p1
#p4_2 = A2* p1 # how come p4_2 is not same as p4
#ef = A[0] *A[1]* A[2]* A3 *p1
#    
#
## Visualizae the result
#plt.figure()
#x = np.array([p1.item(0), p2.item(0), p3.item(0), p4.item(0), ef.item(0)])
#y = np.array([p1.item(1), p2.item(1), p3.item(1), p4.item(1), ef.item(1)])
#plt.plot(x, y, 'o') #plot the joint and end-effector
#plt.plot(x, y,'r') #plot the link
#plt.plot([x[0], x[3]], [y[0], y[3]], 'r') #close the loop
#plt.title('Parallelogram arm chain kinematic visualization')
    




####################################################
# the second configuration



#####################################################

# Input
input_theta1 = 2* np.pi/3
input_theta2 = np.pi/3


# Constraints for close-loop chain based on this configuration
# this constraints is obtained by having the same position from two parts of the chains
theta2 = input_theta2 - input_theta1
theta4 = input_theta1 - input_theta2

# Obtain the first part of the chain (from link 0 - link1'-link2')
# DH params
a = np.array([1,2])
d = np.array([0,0])
alpha = np.array([0,0])
theta = np.array([input_theta1, theta2])

# Transformation matrix from frame i to  frame (i-1), stores in list A
A = list()
num_joints = 2
for i in range(num_joints):
    T = np.matrix([[np.cos(theta[i]), -np.sin(theta[i])*np.cos(alpha[i]), np.sin(alpha[i])*np.sin(alpha[i]), a[i] *np.cos(theta[i])],
                [np.sin(theta[i]), np.cos(theta[i])*np.cos(alpha[i]), -np.cos(theta[i])*np.sin(alpha[i]), a[i]*np.sin(theta[i])],
                [0, np.sin(alpha[i]), np.cos(alpha[i]), d[i]],
                [0, 0, 0, 1]])
    A.append(T)

# Obtain the first part of the chain (from link 0 - link1'-link2')
# DH params
a2 = np.array([2,1])
d2 = np.array([0,0])
alpha2 = np.array([0,0])
theta2 = np.array([input_theta2, theta4])

# Transformation matrix from frame i to  frame (i-1), stores in list A
A2 = list()
num_joints = 2
for i in range(num_joints):
    T = np.matrix([[np.cos(theta2[i]), -np.sin(theta2[i])*np.cos(alpha2[i]), np.sin(alpha2[i])*np.sin(alpha2[i]), a2[i] *np.cos(theta2[i])],
                [np.sin(theta2[i]), np.cos(theta2[i])*np.cos(alpha2[i]), -np.cos(theta2[i])*np.sin(alpha2[i]), a2[i]*np.sin(theta2[i])],
                [0, np.sin(alpha2[i]), np.cos(alpha2[i]), d2[i]],
                [0, 0, 0, 1]])
    A2.append(T)

# Transformation from frame 3 to frame 4 (end-effector)
a3 = 1
A3 = np.matrix([[1, 0, 0, a3],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])


# Calculate the end-effector position and position of each joint
p1 = np.matrix([0, 0, 0, 1])
p1 = p1.transpose()
p2 = A[0]* p1
p3 = A[0] *A[1] *p1
p4 = A2[0]*p1
p3_2 = A2[0]*A2[1]*p1
ef = A[0] *A[1]*A3 *p1


# Visualizae the result
plt.figure()
x = np.array([p1.item(0), p2.item(0), p3.item(0), ef.item(0)])
y = np.array([p1.item(1), p2.item(1), p3.item(1), ef.item(1)])
x2 = np.array([p1.item(0), p4.item(0), p3.item(0)])
y2 = np.array([p1.item(1), p4.item(1), p3.item(1)])
#x = np.array([p1.item(0), p2.item(0), p3.item(0), p4.item(0), ef.item(0)])
#y = np.array([p1.item(1), p2.item(1), p3.item(1), p4.item(1), ef.item(1)])
plt.plot(x, y, 'o') #plot the joint and end-effector
plt.plot(x, y,'r') #plot the link
plt.plot(x2, y2, 'b') #plot the joint and end-effector
plt.plot(x2, y2,'p') #plot the link
#plt.plot([x[0], x[3]], [y[0], y[3]], 'r') #close the loop
plt.title('Parallelogram arm chain kinematic visualization')