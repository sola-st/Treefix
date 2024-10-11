# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity_test.py
from l3.Runtime import _l_
expected = set(expected)
_l_(19623)
actual = set(str(s) for s in actual)
_l_(19624)
self.assertSetEqual(
    expected, actual, 'for symbol set: %s\n'
    '  Expected: %s\n'
    '  Got:      %s\n'
    '  Missing:  %s\n'
    '  Extra:    %s\n' % (name.upper(), expected, actual,
                          expected - actual, actual - expected))
_l_(19625)
