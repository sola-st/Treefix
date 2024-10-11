# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
# GH45263
df = DataFrame([1, 2, 3, 4], [True, None, np.nan, NaT])
result = repr(df)
expected = """      0
True  1
None  2
NaN   3
NaT   4"""
assert result == expected
