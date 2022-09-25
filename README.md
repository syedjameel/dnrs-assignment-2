# dnrs-assignment-2

## Main Task:
1. Jacobian Matrix
2. Finding Singularities

## Bonus Task
1. Bonus Task 2 - https://github.com/syedjameel/dnrs-assignment-2/blob/dnrs-assignment-2/DNRS-%20Home%20task%20(Differential%20kinematics).pdf


## Description:
This Assignment consists of multiple files. Calculations are done in the separate module i.e. SimpleTranformations.py and StanfordManipulatorKinematics.py.
And this tasks are run by a single driver code stanford_manipulator_zxz_jacobian.py in the main folder.


## How to run:
1. clone this branch : https://github.com/syedjameel/dnrs-assignment-2.git
2. go to ~/dnrs-assignment-2 folder
3. In terminal run $ pip3 install -r requirements.txt
3. In terminal run $ python3 stanford_manipulator_zxz_jacobian.py


## Testing:
In the stanford_manipulator_zxz_jacobian.py file you can see the Joint Coordinates t1, t2, d3, t4, t5, t6 and Link Lengths as d2, d6.

First the program will execute the Main task of this assignment i.e. It will compute the Jacobian Matrix based on the forward kinematics,
And then it will check whether there are singularities in the current given Joint Coordinates which are t1=90, t2=90, d3=1, t4=90, t5=90, t6=90,
These joint coordinates values can be changed in the stanford_manipulator_zxz_jacobian.py as per your need.

Furthermore, the program will execute the Bonus task of this assignment i.e. It will compute the Jacobian Matrix Numerically,
Then we will compare both the matrices to be same in the end.


Finally, Open for improvements.

Thanks for reading me.
