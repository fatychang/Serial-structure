# Serial-structure
 Python script for simple serial structure kinematic calculation.

## Serial open chain structure
In the serialKinematic.py script, it calculates the kinematics of the serial configuration based on the D-H convention.
It contains the example from 1 joint to 3 joints.
The configuration of each joint and link will be displayed in the visualization plot.

## Parallogram close lope chain
@brief this script calculates the forwrad kinematic of a parallelgram close-loop model.
 There will be two configuartion used in this script.
 The first configuration has the cut-off point at the last joint (joint4)
 The second configuration has the cut-off point at the third joint counted from either direction.


@author: jschang



## Noted.
1. All the theta input in any configuration is with respect to the base (global frame). However, the joint angle from the D-H method is rotation angle from the local frame.