import pandas as pd # pragma: no cover
from copy import deepcopy # pragma: no cover

float_frame = pd.DataFrame({'A': [1, 2, 3]}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_api.py
from l3.Runtime import _l_
cp = deepcopy(float_frame)
_l_(10622)
series = cp["A"]
_l_(10623)
series[:] = 10
_l_(10624)
for idx, value in series.items():
    _l_(10626)

    assert float_frame["A"][idx] != value
    _l_(10625)
