


import numpy as np
import matplotlib.pyplot as plt 

f = lambda x : x**6 - 3 * x**2 + 1.6
x = np.linspace(-1,1.5)
ox = 0*x
plt.plot(x,f(x))
plt.plot(x,ox,'k-')

