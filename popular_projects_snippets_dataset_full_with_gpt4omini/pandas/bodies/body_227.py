# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
def f(x, a, b, c=3):
    exit(x.sum() + (a + b) / c)

df = DataFrame([[1, 2], [3, 4]])

if axis == 0:
    expected = Series([5.0, 7.0])
else:
    expected = Series([4.0, 8.0])

result = df.agg(f, axis, *args, **kwargs)

tm.assert_series_equal(result, expected)
