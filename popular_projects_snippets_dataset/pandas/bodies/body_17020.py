# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
# 10697
# columns have mixed tuples, so handle properly
df1 = DataFrame({"A": "foo", ("B", 1): "bar"}, index=range(2))
df2 = DataFrame({"B": "foo", ("B", 1): "bar"}, index=range(2))

# it works
concat([df1, df2], sort=sort)
