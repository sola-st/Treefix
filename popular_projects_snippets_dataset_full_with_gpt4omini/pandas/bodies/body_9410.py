# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_arithmetic.py
# https://github.com/pandas-dev/pandas/issues/27398, GH#22793
a = pd.array([0, 1, -1, None], dtype="Int64")
result = a / zero
expected = FloatingArray(
    np.array([np.nan, np.inf, -np.inf, 1], dtype="float64"),
    np.array([False, False, False, True]),
)
if negative:
    expected *= -1
tm.assert_extension_array_equal(result, expected)
