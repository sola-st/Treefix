# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
index = pd.Index([3, 4], name="xyz")
obj = pd.Series(self.rep[from_key], index=index, name="yyy")
assert obj.dtype == from_key

result = obj.replace(replacer)

exp = pd.Series(self.rep[to_key], index=index, name="yyy")
assert exp.dtype == to_key

tm.assert_series_equal(result, exp)
