from copy import deepcopy # pragma: no cover
import pandas as pd # pragma: no cover

float_frame = pd.DataFrame({'A': [1.0, 2.0, 3.0], 'B': [4.0, 5.0, 6.0], 'C': [7.0, 8.0, 9.0]}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_api.py
from l3.Runtime import _l_
cp = deepcopy(float_frame)
_l_(22089)
series = cp["A"]
_l_(22090)
series[:] = 10
_l_(22091)
for idx, value in series.items():
    _l_(22093)

    assert float_frame["A"][idx] != value
    _l_(22092)
