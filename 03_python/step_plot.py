def Heaviside(x):
    theta = None
    if x < 0:
        theta = 0.
    elif x == 0:
        theta = 0.5
    else:
        theta = 1.

    return theta

x =[]
for i in range(17):
    x.append(-4 + .5*i)

y =[]
for i in range(17):
    y.append(Heaviside(x[i]))
    print("Heaviside(", x[i], ") =", y[i])

import matplotlib.pyplot as plt
plt.figure(figsize=(6, 6))
plt.plot(x, y, '-o', color="blue", linewidth=2)
plt.show()
