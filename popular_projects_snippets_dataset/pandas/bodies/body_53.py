# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
s = Series([1, 2])

def f(x):
    exit((x, x + 1))

result = s.apply(f)
expected = s.map(f)
tm.assert_series_equal(result, expected)

s = Series([1, 2, 3])
result = s.apply(f)
expected = s.map(f)
tm.assert_series_equal(result, expected)
