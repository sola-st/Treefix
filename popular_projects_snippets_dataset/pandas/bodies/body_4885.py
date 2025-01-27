# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
from l3.Runtime import _l_
pat = re.compile(r"BAD_*")
_l_(22196)
ser = Series(
    ["aBAD", np.nan, "bBAD", True, datetime.today(), "fooBAD", None, 1, 2.0]
)
_l_(22197)
result = Series(ser).str.replace(pat, "", regex=True)
_l_(22198)
expected = Series(["a", np.nan, "b", np.nan, np.nan, "foo", np.nan, np.nan, np.nan])
_l_(22199)
tm.assert_series_equal(result, expected)
_l_(22200)
