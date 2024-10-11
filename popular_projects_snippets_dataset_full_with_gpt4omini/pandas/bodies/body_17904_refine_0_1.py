import warnings # pragma: no cover
import pytest # pragma: no cover

tm = pytest # pragma: no cover
_f2 = lambda old: warnings.warn('This is a FutureWarning', FutureWarning) or old # pragma: no cover
key = 'test_key' # pragma: no cover

import warnings # pragma: no cover
from unittest.mock import Mock # pragma: no cover

tm = Mock() # pragma: no cover
tm.assert_produces_warning = Mock() # pragma: no cover
_f2 = lambda old: warnings.warn('This is a FutureWarning', FutureWarning) or old # pragma: no cover
key = 'test_key' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/util/test_deprecate_kwarg.py
from l3.Runtime import _l_
with tm.assert_produces_warning(FutureWarning):
    _l_(10174)

    assert _f2(old=key) == key
    _l_(10173)
