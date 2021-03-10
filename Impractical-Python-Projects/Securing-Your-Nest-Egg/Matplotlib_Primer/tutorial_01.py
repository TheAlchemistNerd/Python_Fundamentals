import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2.0*np.pi, 101)
y = np.sin(x)
z = np.sinh(x)

# separate figure object and axes object
# from plotting object
fig, ax1 = plt.subplots()

# Duplicate the axes with a diff y axis
# and the same x axis
ax2 = ax1.twinx()

# plot the curves on axes 1, and 2 nd get the curve handles
curve1 = ax1.plot(x, y, label="sin", color='r' )
curve2 = ax2.plot(x, z, label="sinh", color='b' )

# Make the curves list to access the parameters in the curves
curves = [curve1, curve2]

# add legend via ax1 or ax2 object
# one command is usually sufficient
# ax1.legend(curves, [curve.get_label() for curve in curves])
# global figure properties
plt.title("Plot of sine and hyperbolic sine")
plt.show()