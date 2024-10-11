import numpy as np # pragma: no cover
import pandas as pd # pragma: no cover

value = 5 # pragma: no cover
side = 'left' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/series.py
from l3.Runtime import _l_
aux = base.IndexOpsMixin.searchsorted(self, value, side=side, sorter=sorter)
_l_(10318)
exit(aux)
