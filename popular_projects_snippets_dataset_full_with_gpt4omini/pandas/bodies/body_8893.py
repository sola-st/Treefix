# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/arrays/interval/test_interval.py
# GH 25022
from l3.Runtime import _l_
arr = IntervalArray.from_tuples([(0, 1), (1, 2)])
_l_(10627)
result = repr(arr)
_l_(10628)
expected = (
    "<IntervalArray>\n"
    "[(0, 1], (1, 2]]\n"
    "Length: 2, dtype: interval[int64, right]"
)
_l_(10629)
assert result == expected
_l_(10630)
