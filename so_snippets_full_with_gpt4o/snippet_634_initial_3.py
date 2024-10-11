import numpy as np # pragma: no cover
from scipy.interpolate import interp2d # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/36013063/what-is-the-purpose-of-meshgrid-in-python-numpy
from l3.Runtime import _l_
def sinus2d(x, y):
    _l_(13953)

    aux = np.sin(x) + np.sin(y)
    _l_(13952)
    return aux

xx, yy = np.meshgrid(np.linspace(0,2*np.pi,100), np.linspace(0,2*np.pi,100))
_l_(13954)
z = sinus2d(xx, yy) # Create the image on this grid
_l_(13955) # Create the image on this grid
try:
    import matplotlib.pyplot as plt
    _l_(13957)

except ImportError:
    pass
plt.imshow(z, origin='lower', interpolation='none')
_l_(13958)
plt.show()
_l_(13959)

z2 = sinus2d(np.linspace(0,2*np.pi,100)[:,None], np.linspace(0,2*np.pi,100)[None,:])
_l_(13960)

condition = z>0.6
_l_(13961)
z_new = z[condition] # This will make your array 1D
_l_(13962) # This will make your array 1D

x_new = xx[condition]
_l_(13963)
y_new = yy[condition]
_l_(13964)
try:
    from scipy.interpolate import interp2d
    _l_(13966)

except ImportError:
    pass
interpolated = interp2d(x_new, y_new, z_new)
_l_(13967)

interpolated_grid = interpolated(xx[0], yy[:, 0]).reshape(xx.shape)
_l_(13968)

