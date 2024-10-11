import pytest # pragma: no cover
import pandas as pd # pragma: no cover

class MockDataFrame: # pragma: no cover
    def add_prefix(self, *args, **kwargs): # pragma: no cover
        axis = kwargs.get('axis', None) # pragma: no cover
        if axis == 2: # pragma: no cover
            raise ValueError('No axis named 2 for object type DataFrame') # pragma: no cover
    def add_suffix(self, *args, **kwargs): # pragma: no cover
        axis = kwargs.get('axis', None) # pragma: no cover
        if axis == 2: # pragma: no cover
            raise ValueError('No axis named 2 for object type DataFrame') # pragma: no cover
float_frame = MockDataFrame() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_add_prefix_suffix.py
from l3.Runtime import _l_
with pytest.raises(ValueError, match="No axis named 2 for object type DataFrame"):
    _l_(16387)

    float_frame.add_prefix("foo#", axis=2)
    _l_(16386)

with pytest.raises(ValueError, match="No axis named 2 for object type DataFrame"):
    _l_(16389)

    float_frame.add_suffix("foo#", axis=2)
    _l_(16388)
