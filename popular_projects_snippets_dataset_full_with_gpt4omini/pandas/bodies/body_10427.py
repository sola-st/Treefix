# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
# GH 16771
# cython transforms with more groups than rows
x_vals = [1]
x_cats = range(2)
y = [1]
df = DataFrame({"x": Categorical(x_vals, x_cats), "y": y})
result = getattr(df.y.groupby(df.x), func)()
expected = df.y
tm.assert_series_equal(result, expected)
