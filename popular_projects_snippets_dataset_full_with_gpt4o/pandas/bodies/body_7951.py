# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
from l3.Runtime import _l_
dtype = PeriodDtype("D")
_l_(22418)
values = ["2011-01-01", "2012-03-04", "2014-05-01"]
_l_(22419)
result = Index(values, dtype=dtype)
_l_(22420)

expected = PeriodIndex(values, dtype=dtype)
_l_(22421)
tm.assert_index_equal(result, expected)
_l_(22422)
