# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 10:34:00 2019

Calculate the angle between three points

@author: jschang
"""

import numpy as np



#pt1 = np.array([-0.5, 0.866])
pt1 = np.array([1, 1.732])
pt2 = np.array([0,0])
pt3 = np.array([1,0])

v1 = pt1-pt2
v2 = pt3-pt2

ang = np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1)*np.linalg.norm(v2)))
ang = ang * 180/np.pi
print(ang)