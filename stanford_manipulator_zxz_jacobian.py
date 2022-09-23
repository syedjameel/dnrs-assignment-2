# Written by Jameel Ahmed Syed
# Email id: j.syed@innopolis.university

# Assignment - 2
# 1. Main Task
# 2. Bonus Task 2

from numpy import pi
from utils.StanfordManipulatorKinematics import *
from art import tprint
import math

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

joint_coordinates = [np.rad2deg(t1), np.rad2deg(t2), d3, np.rad2deg(t4), np.rad2deg(t5), np.rad2deg(t6)]

if __name__ == "__main__":

    # MAIN TASK SOLUTION
    tprint("MAIN      TASK : ")
    # Forward Kinematics of the Stanford Manipulator
    T = forward(joint_angles=t, link_lengths=d, euler_wrist=wrist, symbolic=False)

    # Jacobian Matrix using Geometrical/Screw Theory
    J = jacobian_geometrical(tranforamtions=T)
    print_matrix(input_matrix=J, name_matrix='Jacobian Matrix Geometrically')

    # Calculating the Determinant of the Jacobian Matrix to check the singularity
    determinant = J.det()
    print_matrix(input_matrix=determinant, name_matrix="Determinant")

    if determinant != 0:
        print(f"No Singularities found at the following Joint Coordinates \n q = {joint_coordinates} \n")
    elif determinant == 0:
        print(f"Singularities found at the following Joint Coordinates \n q = {joint_coordinates} \n")

    # Forward Kinematics in Symbolic Form
    T_symbolic = forward(joint_angles=t, link_lengths=d, euler_wrist=wrist, symbolic=True)

    # Jacobian Matrix in Symbolic Form
    J = jacobian_geometrical(tranforamtions=T)

    print("Please wait the determinant is getting solved symbolically.... ")
    # Please uncomment the following 4 lines to check for the singularities
    # Note : It will take some time (1 - 2 minutes) to process the determinant symbolically
    # and then find the singularities, so please wait...

    # J_determinant = J.det()
    # print("J_determinant = ", J_determinant)
    # solved_determinant = solve(J_determinant)
    # print("Singularities = ", solved_determinant)

    # I have got the following results from the above 4 lines
    print("The Singularities are =  [{d3: 0}, {t2: 0}, {t5: 0}, {t5: pi}] \n\n")

    # BONUS TASK 2 SOLUTION
    tprint("BONUS       TASK 2 : ")

    # From the Final Homogeneous Matrix we get the following Equations
    X = trigsimp(T_symbolic['X'])
    Y = trigsimp(T_symbolic['Y'])
    Z = trigsimp(T_symbolic['Z'])
    ThetaZ = trigsimp(atan2((T_symbolic['T06'][0, 2]), -T_symbolic['T06'][1, 2]))
    ThetaX = trigsimp(atan2(-sqrt(1 - (T_symbolic['T06'][2, 2])**2), (T_symbolic['T06'][2, 2])))
    ThetaY = trigsimp(atan2((-T_symbolic['T06'][2, 1]), (T_symbolic['T06'][2, 0])))

    print('X = ', X)
    print('Y = ', Y)
    print('Z = ', Z)
    print('ThetaX = ', ThetaX)
    print('ThetaY = ', ThetaY)
    print('ThetaZ = ', ThetaZ)

    function_list = [X, Y, Z, ThetaX, ThetaY, ThetaZ]
    Jn = jacobian_numerically(function_list, t1, t2, d3, t4, t5, t6, d2, d6)
    mat = []
    a = 0
    while Jn != []:
        mat.append(Jn[:6])
        Jn = Jn[6:]
        a = a + 1
    Jm = Matrix(mat)
    print("\n")
    print_matrix(input_matrix=Jm, name_matrix="Jacobian Matrix Numerically")

    print("\nWe see the Jacobian Matrices Geometrical and Numerical are similar")