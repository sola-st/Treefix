import numpy as np # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3584805/what-does-the-argument-mean-in-fig-add-subplot111
from l3.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(909)

except ImportError:
    pass
plt.figure(figsize=(8,8))
_l_(910)
plt.subplot(3,2,1)
_l_(911)
plt.subplot(3,2,3)
_l_(912)
plt.subplot(3,2,5)
_l_(913)
plt.subplot(2,2,2)
_l_(914)
plt.subplot(2,2,4)
_l_(915)

