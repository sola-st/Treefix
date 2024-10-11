import numpy as np # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/21494489/what-does-numpy-random-seed0-do
from l3.Runtime import _l_
np.random.seed(2)
_l_(14407)
np.random.randn(2) # array([-0.41675785, -0.05626683])
_l_(14408) # array([-0.41675785, -0.05626683])
np.random.randn(1) # array([-1.24528809])
_l_(14409) # array([-1.24528809])

np.random.seed(2)
_l_(14410)
np.random.randn(1) # array([-0.41675785])
_l_(14411) # array([-0.41675785])
np.random.randn(2) # array([-0.05626683, -1.24528809])
_l_(14412) # array([-0.05626683, -1.24528809])

