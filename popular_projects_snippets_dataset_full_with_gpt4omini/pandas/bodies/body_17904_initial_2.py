import warnings # pragma: no cover
import numpy as np # pragma: no cover

class tm:  # Mock class for testing# pragma: no cover
    @staticmethod# pragma: no cover
    def assert_produces_warning(warning_type):# pragma: no cover
        warnings.simplefilter('always')# pragma: no cover
        return warnings.warn('This is a mock warning', warning_type) # pragma: no cover
def _f2(old):# pragma: no cover
    return old  # Mock function that returns the input value # pragma: no cover
key = np.array([1, 2, 3])  # An example numpy array as the key # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/util/test_deprecate_kwarg.py
from l3.Runtime import _l_
with tm.assert_produces_warning(FutureWarning):
    _l_(10174)

    assert _f2(old=key) == key
    _l_(10173)
