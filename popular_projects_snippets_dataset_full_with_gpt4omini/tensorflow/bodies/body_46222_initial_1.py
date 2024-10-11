expected = {'A', 'B', 'C'} # pragma: no cover
actual = ['B', 'D', 'C'] # pragma: no cover
self = type('Mock', (object,), {'assertSetEqual': lambda self, a, b, msg: None})() # pragma: no cover
name = 'test_case' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py
from l3.Runtime import _l_
expected = set(expected)
_l_(6934)
actual = set(str(s) for s in actual)
_l_(6935)
self.assertSetEqual(
    expected, actual, 'for symbol set: %s\n'
    '  Expected: %s\n'
    '  Got:      %s\n'
    '  Missing:  %s\n'
    '  Extra:    %s\n' % (name.upper(), expected, actual,
                          expected - actual, actual - expected))
_l_(6936)
