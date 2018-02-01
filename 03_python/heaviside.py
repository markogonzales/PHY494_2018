# Heaviside step function
import matplotlib.pyplot as plt

x1 = -3
x2 = 0
x3 = 3

theta = None
if x1 < 0:
    theta1 = 0.
elif x1 == 0:
    theta1 = 0.5
else:
    theta1 = 1.

if x2 < 0:
    theta2 = 0.
elif x2 == 0:
    theta2 = 0.5
else:
    theta2 = 1.

if x3 < 0:
    theta3 = 0.
elif x3 == 0:
    theta3 = 0.5
else:
    theta3 = 1.

print("theta(" + str(x1) + ") = " + str(theta1))
