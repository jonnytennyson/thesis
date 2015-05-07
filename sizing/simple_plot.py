import matplotlib.pyplot as plt
import numpy as np
import matplotlib

font = {'size'   : 16}

matplotlib.rc('font', **font)

x = np.arange(1, 10.1, 0.1)
x0 = 10 * x
y0 = 10 * x**0.75
y1 = 10 * x**0.5
y2 = 10 * x**0.25

plt.plot(x, x0, "b", label="linear", linewidth="5")
plt.plot(x, y0, "g", label="linear", linewidth="5")
plt.plot(x, y1, "r", label="logarithmic", linewidth="5")
plt.xlim(1, 10)
plt.ylim(10, 100)

plt.xlabel("Number of Fluorophores")
plt.ylabel("Number of Photons")

#plt.legend()
plt.savefig("multimers.pdf")
plt.show()
