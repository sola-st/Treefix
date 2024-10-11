from unittest.mock import Mock # pragma: no cover

plt = Mock() # pragma: no cover
plt.plot = Mock() # pragma: no cover
plt.legend = Mock() # pragma: no cover
plt.tight_layout = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot
from l3.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(2117)

except ImportError:
    pass

plt.plot([0, 1], [0, 1], label="Label 1")
_l_(2118)
plt.plot([0, 1], [0, 2], label='Label 2')
_l_(2119)

plt.legend(loc=(1.05, 0.5))
_l_(2120)
plt.tight_layout()
_l_(2121)

