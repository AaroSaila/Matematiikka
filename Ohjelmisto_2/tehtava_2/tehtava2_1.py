import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

fig = plt.figure()
ax = fig.subplots()

ymp = plt.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

ax.axis('equal')

plt.xticks([-1, 0, 1], minor=True)
plt.yticks([-1, 0, 1])

pist_xy = np.array

plt.show()