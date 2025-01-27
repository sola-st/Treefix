# Extracted from https://stackoverflow.com/questions/19410042/how-to-make-ipython-notebook-matplotlib-plot-inline
In [1]:  %matplotlib inline
         import matplotlib
         import matplotlib.pyplot as plt
         import numpy as np
In [2]:  x = np.array([1, 3, 4])
         y = np.array([1, 5, 3])
In [3]:  fig = plt.figure()
         <Figure size 432x288 with 0 Axes>                      #this might be the problem
In [4]:  ax = fig.add_subplot(1, 1, 1)
In [5]:  ax.scatter(x, y)
Out[5]:  <matplotlib.collections.PathCollection at 0x12341234>  # CAN'T SEE ANY PLOT :(
In [6]:  plt.show()                                             # STILL CAN'T SEE IT :(

In [1]:  %matplotlib inline
         import matplotlib
         import matplotlib.pyplot as plt
         import numpy as np
In [2]:  x = np.array([1, 3, 4])
         y = np.array([1, 5, 3])
In [3]:  fig = plt.figure()
         ax = fig.add_subplot(1, 1, 1)
         ax.scatter(x, y)
Out[3]:  <matplotlib.collections.PathCollection at 0x12341234>
         # AND HERE APPEARS THE PLOT AS DESIRED :)

