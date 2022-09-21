# Written by Jameel Ahmed Syed
# Email id: j.syed@innopolis.university


from numpy import pi
from utils.StanfordManipulatorKinematics import *

T = []
t1 = pi/2   # Joint Angle 1
t2 = pi/2   # Joint Angle 2
t3 = 0      # Dummy variable for just sequence sake
t4 = pi/2   # Joint Angle 4
t5 = pi/2   # Joint Angle 5
t6 = pi/2   # Joint Angle 6

t = [t1, t2, t3, t4, t5, t6]    # All the Joint angles

d1 = 0      # Dummy variable for just sequence sake
d2 = 1      # Link 2 Length
d3 = 1      # Prismatic Joint length + the Link 3 Length
d4 = 0      # Dummy variable for just sequence sake
d5 = 0      # Dummy variable for just sequence sake
d6 = 1      # Wrist to the end effector Length

d = [d1, d2, d3, d4, d5, d6]    # All the Link Lengths

wrist = ['z', 'x', 'z']     # Euler's Wrist Configuration (xyz, xzy, xyx, xzx, yxz, yzx, yxy, yzy, zxy, zyx, zyz, zxz)


if __name__ == "__main__":

    # Forward Kinematics in Numerical Form
    T = forward(joint_angles=t, link_lengths=d, euler_wrist=wrist, symbolic=False)
    for key, val in T.items():
        print_matrix(input_matrix=val, name_matrix=key)

    # Forward Kinematics in Symbolic Form
    T = forward(joint_angles=t, link_lengths=d, euler_wrist=wrist, symbolic=True)
    for key, val in T.items():
        print_matrix(input_matrix=val, name_matrix=key)

    




