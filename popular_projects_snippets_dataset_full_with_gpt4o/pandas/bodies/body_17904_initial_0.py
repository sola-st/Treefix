import warnings # pragma: no cover

tm = type('Mock', (object,), {'assert_produces_warning': lambda self, warning_type: warnings.catch_warnings()})() # pragma: no cover
_f2 = lambda old: old # pragma: no cover
key = 'example_key' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/util/test_deprecate_kwarg.py
from l3.Runtime import _l_
with tm.assert_produces_warning(FutureWarning):
    _l_(20899)

    assert _f2(old=key) == key
    _l_(20898)
