# Heaviside step function

def heaviside(x):
   """Heaviside step function"""

   theta = None
   if x < 0:
      theta = 0.
   elif x == 0:
      theta = 0.5
   else:
      theta = 1.

   return theta

def fahrenheit2kelvin(t):
    T = (t - 32) * (5/9) + 273.15
    return T
def kelvin2celsius(t1):
    T1 = t1 - 273.15
    return T1
    
