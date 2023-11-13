import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6.4*3, 4.8*3))

X = np.linspace(-np.pi*3, np.pi*3, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

ax.set_xticks(np.arange(-np.pi*3, np.pi*3, np.pi), ["-3π", "-2π", "-π", "0", "π", "2π"])

plt.plot(X,C, color="blue", linestyle="--", label="cos(x)")
plt.plot(X,S, color="red", linewidth=5, label="sin(x)")

ax.set_xlabel("x-akseli")
ax.set_ylabel("y-akseli")
ax.set_title("kaavio")
ax.legend()

plt.show()
