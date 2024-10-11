# Extracted from ./data/repos/pandas/pandas/tests/test_expressions.py
# https://github.com/pandas-dev/pandas/issues/36047
expr._MIN_ELEMENTS = 0
data = np.arange(-50, 50)
obj = box(data)
method = getattr(obj, op)
result = method(scalar)

# compare result with numpy
with option_context("compute.use_numexpr", False):
    expected = method(scalar)

tm.assert_equal(result, expected)

# compare result element-wise with Python
for i, elem in enumerate(data):
    if box == DataFrame:
        scalar_result = result.iloc[i, 0]
    else:
        scalar_result = result[i]
    try:
        expected = getattr(int(elem), op)(scalar)
    except ZeroDivisionError:
        pass
    else:
        assert scalar_result == expected
