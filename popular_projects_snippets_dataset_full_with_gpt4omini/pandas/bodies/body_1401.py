# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py

# across dtypes
df = DataFrame([[1, 2, 1.0, 2.0, 3.0, "foo", "bar"]], columns=list("aaaaaaa"))
df.head()
str(df)
result = DataFrame([[1, 2, 1.0, 2.0, 3.0, "foo", "bar"]])
result.columns = list("aaaaaaa")  # GH#3468

# GH#3509 smoke tests for indexing with duplicate columns
df.iloc[:, 4]
result.iloc[:, 4]

tm.assert_frame_equal(df, result)
