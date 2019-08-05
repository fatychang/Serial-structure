# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 11:16:03 2019

This script calculate the kinematics of the serial configuration based on the D-H convention


@author: jschang
"""

# Import
import numpy as np



##### One link chain (one joint, i=1)
# D-H parameters
a_1 = 1
d_1 = 0
alpha_1 = 0
theta_1 = np.pi/4

# Transformation matrix from frame i to  frame (i-1)
