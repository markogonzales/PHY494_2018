# constants.py

pi = 3.14159
h = 6.62606957e-34

# direct import
from constants import h, pi
h_bar = h / (2*pi)

# aliasing
import constants as c
h_bar = c.h / (2*c.pi)
