import sys # pragma: no cover
import types # pragma: no cover

sys.modules['matplotlib'] = types.ModuleType('matplotlib') # pragma: no cover
sys.modules['matplotlib.pyplot'] = types.ModuleType('pyplot') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3584805/what-does-the-argument-mean-in-fig-add-subplot111
from l3.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(12401)

except ImportError:
    pass
plt.figure(figsize=(8,8))
_l_(12402)
plt.subplot(3,2,1)
_l_(12403)
plt.subplot(3,2,3)
_l_(12404)
plt.subplot(3,2,5)
_l_(12405)
plt.subplot(2,2,2)
_l_(12406)
plt.subplot(2,2,4)
_l_(12407)

