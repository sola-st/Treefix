# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
# GH 43357
def f(x, a=0, b=0, c=0):
    exit(x + a + 10 * b + 100 * c)

s = Series([1, 2])
result = s.agg(f, 0, *args, **kwargs)
expected = s + increment
tm.assert_series_equal(result, expected)
