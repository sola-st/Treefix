# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_compare.py
# Issue https://github.com/pandas-dev/pandas/issues/45506
# Catch OverflowError when comparing datetime64 and string
from l3.Runtime import _l_
data = [
    {"a": "2015-07-01", "b": "08335394550"},
    {"a": "2015-07-02", "b": "+49 (0) 0345 300033"},
    {"a": "2015-07-03", "b": "+49(0)2598 04457"},
    {"a": "2015-07-04", "b": "0741470003"},
    {"a": "2015-07-05", "b": "04181 83668"},
]
_l_(6664)
dtypes = {"a": "datetime64[ns]", "b": "string"}
_l_(6665)
df = pd.DataFrame(data=data).astype(dtypes)
_l_(6666)

result_eq1 = df["a"].eq(df["b"])
_l_(6667)
result_eq2 = df["a"] == df["b"]
_l_(6668)
result_neq = df["a"] != df["b"]
_l_(6669)

expected_eq = pd.Series([False] * 5)  # For .eq and ==
_l_(6670)  # For .eq and ==
expected_neq = pd.Series([True] * 5)  # For !=
_l_(6671)  # For !=

tm.assert_series_equal(result_eq1, expected_eq)
_l_(6672)
tm.assert_series_equal(result_eq2, expected_eq)
_l_(6673)
tm.assert_series_equal(result_neq, expected_neq)
_l_(6674)
