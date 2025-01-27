# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_empty.py

# xref to #12411
# xref to #12045
# xref to #11594
# see below

# 10571
df1 = DataFrame(data=[[1, None], [2, None]], columns=["a", "b"])
df2 = DataFrame(data=[[3, None], [4, None]], columns=["a", "b"])
result = concat([df1, df2])
expected = df1.dtypes
tm.assert_series_equal(result.dtypes, expected)
