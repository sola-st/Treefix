# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
index = pd.Index([3, 4], name="xyz")
obj = pd.Series(self.rep[from_key], index=index, name="yyy")
assert obj.dtype == from_key

result = obj.replace(replacer)

exp = pd.Series(self.rep[to_key], index=index, name="yyy")
if isinstance(obj.dtype, pd.DatetimeTZDtype) and isinstance(
    exp.dtype, pd.DatetimeTZDtype
):
    # with mismatched tzs, we retain the original dtype as of 2.0
    exp = exp.astype(obj.dtype)
else:
    assert exp.dtype == to_key

tm.assert_series_equal(result, exp)
