import pytest # pragma: no cover
import pandas as pd # pragma: no cover

float_frame = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_add_prefix_suffix.py
from l3.Runtime import _l_
with pytest.raises(ValueError, match="No axis named 2 for object type DataFrame"):
    _l_(5915)

    float_frame.add_prefix("foo#", axis=2)
    _l_(5914)

with pytest.raises(ValueError, match="No axis named 2 for object type DataFrame"):
    _l_(5917)

    float_frame.add_suffix("foo#", axis=2)
    _l_(5916)
