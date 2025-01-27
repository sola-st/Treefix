# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_interpolate.py
df = DataFrame(
    {
        "A": [1, 2, np.nan, 4],
        "B": [1, 4, 9, np.nan],
        "C": [1, 2, 3, 5],
        "D": list("abcd"),
    }
)
msg = (
    r"method must be one of \['linear', 'time', 'index', 'values', "
    r"'nearest', 'zero', 'slinear', 'quadratic', 'cubic', "
    r"'barycentric', 'krogh', 'spline', 'polynomial', "
    r"'from_derivatives', 'piecewise_polynomial', 'pchip', 'akima', "
    r"'cubicspline'\]. Got 'not_a_method' instead."
)
with pytest.raises(ValueError, match=msg):
    df.interpolate(method="not_a_method")
