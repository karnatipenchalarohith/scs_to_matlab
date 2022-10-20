import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()

with open('yourfile.txt') as f:
    lines_after_17 = f.readlines()[17:]
