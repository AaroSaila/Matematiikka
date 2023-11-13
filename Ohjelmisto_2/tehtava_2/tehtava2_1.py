import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# Creates the figure and axes.
fig = plt.figure()
ax = fig.subplots()

# Creates the circle
ymp = plt.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)

# Moves left y-axis and bottom x-axis to the center.
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes.
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.axis('equal')

# Creates number ticks. x-axis includes minor ticks in between.
plt.xticks([-1, 0, 1], minor=True)
plt.yticks([-1, 0, 1])

pist_xy = np.array(np.radians([30, 45, 60, 90, 120, 150, 180, 270]))

x = np.cos(pist_xy)
y = np.sin(pist_xy)

plt.scatter(x, y, marker="X")

plt.show()
