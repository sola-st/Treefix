import warnings # pragma: no cover
import pytest # pragma: no cover

tm = pytest # pragma: no cover
_f2 = lambda old: warnings.warn('This is a FutureWarning', FutureWarning) or old # pragma: no cover
key = 'test_key' # pragma: no cover

import warnings # pragma: no cover
from unittest import mock # pragma: no cover

class TM:  # A mock implementation for assert_produces_warning # pragma: no cover
    @staticmethod # pragma: no cover
    def assert_produces_warning(warning_class): # pragma: no cover
        return mock.patch('warnings.warn', side_effect=lambda msg, category: msg if category == warning_class else None) # pragma: no cover
tm = TM() # pragma: no cover
_f2 = lambda old: warnings.warn('This is a FutureWarning', FutureWarning) or old # pragma: no cover
key = 'test_key' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/util/test_deprecate_kwarg.py
from l3.Runtime import _l_
with tm.assert_produces_warning(FutureWarning):
    _l_(10174)

    assert _f2(old=key) == key
    _l_(10173)
