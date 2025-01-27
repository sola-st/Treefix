# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# GH#35529
box = box_with_array
xbox = np.ndarray if box is pd.array else box

left = Series([1000, 222330, 30], dtype="timedelta64[ns]")
right = Series([1000, 222330, None], dtype="timedelta64[ns]")

left = tm.box_expected(left, box)
right = tm.box_expected(right, box)

expected = np.array([1.0, 1.0, np.nan], dtype=np.float64)
expected = tm.box_expected(expected, xbox)
if box is DataFrame and using_array_manager:
    # INFO(ArrayManager) floordiv returns integer, and ArrayManager
    # performs ops column-wise and thus preserves int64 dtype for
    # columns without missing values
    expected[[0, 1]] = expected[[0, 1]].astype("int64")

with tm.maybe_produces_warning(
    RuntimeWarning, box is pd.array, check_stacklevel=False
):
    result = left // right

tm.assert_equal(result, expected)

# case that goes through __rfloordiv__ with arraylike
with tm.maybe_produces_warning(
    RuntimeWarning, box is pd.array, check_stacklevel=False
):
    result = np.asarray(left) // right
tm.assert_equal(result, expected)
