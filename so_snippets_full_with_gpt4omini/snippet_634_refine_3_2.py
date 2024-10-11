import numpy as np # pragma: no cover

np = type('Mock', (object,), {'sin': np.sin, 'meshgrid': np.meshgrid, 'linspace': np.linspace, 'pi': np.pi})() # pragma: no cover

import numpy as np # pragma: no cover

np = type('Mock', (object,), {'sin': np.sin, 'meshgrid': np.meshgrid, 'linspace': staticmethod(lambda start, stop, num: [start + (stop - start) * i / (num - 1) for i in range(num)]), 'pi': 3.141592653589793})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/36013063/what-is-the-purpose-of-meshgrid-in-python-numpy
from l3.Runtime import _l_
def sinus2d(x, y):
    _l_(1679)

    aux = np.sin(x) + np.sin(y)
    _l_(1678)
    return aux

xx, yy = np.meshgrid(np.linspace(0,2*np.pi,100), np.linspace(0,2*np.pi,100))
_l_(1680)
z = sinus2d(xx, yy) # Create the image on this grid
_l_(1681) # Create the image on this grid
try:
    import matplotlib.pyplot as plt
    _l_(1683)

except ImportError:
    pass
plt.imshow(z, origin='lower', interpolation='none')
_l_(1684)
plt.show()
_l_(1685)

z2 = sinus2d(np.linspace(0,2*np.pi,100)[:,None], np.linspace(0,2*np.pi,100)[None,:])
_l_(1686)

condition = z>0.6
_l_(1687)
z_new = z[condition] # This will make your array 1D
_l_(1688) # This will make your array 1D

x_new = xx[condition]
_l_(1689)
y_new = yy[condition]
_l_(1690)
try:
    from scipy.interpolate import interp2d
    _l_(1692)

except ImportError:
    pass
interpolated = interp2d(x_new, y_new, z_new)
_l_(1693)

interpolated_grid = interpolated(xx[0], yy[:, 0]).reshape(xx.shape)
_l_(1694)

