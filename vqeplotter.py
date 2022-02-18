import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pandas

forcedcost = pandas.read_csv('brutevcost.csv', header=None)
vqecost = pandas.read_csv('vqecost.csv', header=None)

plt.plot(range(109), forcedcost, label='forced')
plt.plot(range(109), vqecost, label='VQE')
plt.legend()
plt.xlabel('Iterations')
plt.ylabel('Cost')
plt.show()
