# Extracted from ./data/repos/pandas/pandas/tests/frame/test_subclass.py
# https://github.com/pandas-dev/pandas/pull/34402
# allow subclass in both directions
df1 = DataFrame({"a": [1, 2, 3]})
df2 = tm.SubclassedDataFrame({"a": [1, 2, 3]})
assert df1.equals(df2)
assert df2.equals(df1)
