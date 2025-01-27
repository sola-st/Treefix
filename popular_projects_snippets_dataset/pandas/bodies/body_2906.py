# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_equals.py
# see GH#28839
df1 = DataFrame({"a": [1, 2], "b": ["s", "d"]})
df2 = DataFrame({"a": ["s", "d"], "b": [1, 2]})
assert df1.equals(df2) is False
