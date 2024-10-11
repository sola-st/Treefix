import pandas as pd # pragma: no cover

x = pd.DataFrame() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/window/moments/test_moments_consistency_expanding.py
from l3.Runtime import _l_
aux = x.isnull().all().all()
_l_(10621)
exit(aux)
