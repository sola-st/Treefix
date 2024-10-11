# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH8909
m = map(lambda x: x, range(10))

result = Series(m)
exp = Series(range(10))
tm.assert_series_equal(result, exp)

# same but with non-default index
m = map(lambda x: x, range(10))
result = Series(m, index=range(10, 20))
exp.index = range(10, 20)
tm.assert_series_equal(result, exp)
