# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 17:56:00 2019

@author: jschang
"""


import numpy as np
import matplotlib.pyplot as plt



########################
##  INV KINEMATIC     ##
########################

# Known end-effector position
ef = np.array([1,3.4641])
phi = np.pi/3


# Design params
length = np.array([1,2,1])


# phi = input_theta1 + theta2 = input_theta2 (since theta2=input_theta2-input_theta1)
input_theta2 = phi

# cos(theta2) = [(Bx)^2 + (By)^2 - l1^2 - l2^2] / (2*l1*l2)
Bx = ef[0] - length[2] * np.cos(input_theta2)
By = ef[1] - length[2] * np.sin(input_theta2)

cos_theta2 = (np.square(Bx) + np.square(By) - np.square(length[0]) - np.square(length[1])) / (2*length[0]*length[1])

# There will be two results for theta2, take the negative one since theta2 = theta1'1-theta1' (usually theta1' is greater than theta1'')
theta2 = np.arccos(cos_theta2) * -1


print('theta2:{}'.format(theta2*180/np.pi))

input_theta1 = input_theta2 - theta2

# print out the result
print('input_theta1:{}'.format(input_theta1*180/np.pi))
print('input_theta2:{}'.format(input_theta2*180/np.pi))