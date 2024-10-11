import pandas as pd # pragma: no cover

ddof = 1 # pragma: no cover
numeric_only = True # pragma: no cover
engine = 'python' # pragma: no cover
engine_kwargs = {} # pragma: no cover

import pandas as pd # pragma: no cover

class Mock: pass # pragma: no cover
mock_instance = Mock() # pragma: no cover
ddof = 1 # pragma: no cover
numeric_only = True # pragma: no cover
engine = 'python' # pragma: no cover
engine_kwargs = {} # pragma: no cover
super = lambda: mock_instance # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/core/window/expanding.py
from l3.Runtime import _l_
aux = super().var(
    ddof=ddof,
    numeric_only=numeric_only,
    engine=engine,
    engine_kwargs=engine_kwargs,
)
_l_(9386)
exit(aux)
