import matplotlib.pyplot as plt
import numpy as np

ind = np.arange(5)
width = .75
shell = 8.853
fork = 0.625247001648
load = 0.0756311416626
shared = 0.000869035720825
optimal = 0.000123023986816


times = [shell, fork, load, shared, optimal]
labels = ["fork & exec", "fork", "reload", "c & r", "optimal"]

fig, ax = plt.subplots()
plot = ax.bar(ind, times, width, log=True)

ax.set_xticks(ind + .35)
ax.set_xticklabels(labels)
ax.set_ylabel("Time (s)")
ax.set_xlabel("Isolation technique")
ax.set_title('Time for 1000 "empty function" invocations')
plt.show()
