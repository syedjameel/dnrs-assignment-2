# Written by Jameel Ahmed Syed
# Email id: j.syed@innopolis.university
import sympy
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

    # Forward Kinematics of the Stanford Manipulator
    T = forward(joint_angles=t, link_lengths=d, euler_wrist=wrist, symbolic=False)
    #for key, val in T.items():         # Uncomment these two lines to print all the transformations
    #    print_matrix(input_matrix=val, name_matrix=key)

    # Jacobian Matrix Geometrically/Screw Theory
    J = jacobian_geometrical(tranforamtions=T)
    print_matrix(input_matrix=J, name_matrix='Jacobian Matrix')

    # Calculating the Determinant of the Jacobian Matrix to check the singularity
    determinant = J.det()
    print_matrix(input_matrix=determinant, name_matrix="Determinant: ")

    if determinant != 0:
        print(f"The Jacobian Matrix is Non-Singular")
    elif determinant == 0:
        print(f"The Jacobian Matrix is Singular")


    # Solve the determinant of jacobian to be zero to get the singularities

    


    # Forward Kinematics in Symbolic Form
    T = forward(joint_angles=t, link_lengths=d, euler_wrist=wrist, symbolic=True)
    for key, val in T.items():
        print_matrix(input_matrix=val, name_matrix=key)

    J = jacobian_geometrical(tranforamtions=T)
    print_matrix(input_matrix=J, name_matrix='J')
    #for key, val in J.items():
    #    print_matrix(input_matrix=val, name_matrix=key)

    determinant = J.det()
    print("\n\n")
    print("Deter = ", determinant)
    print_matrix(input_matrix=determinant, name_matrix="Determinant: ")

    




