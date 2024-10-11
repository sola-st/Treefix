# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# If we don't ravel/reshape around ensure_str_array, we end up
#  with an array of strings each of which is e.g. "[0 1 2]"
arr = np.arange(12).reshape(4, 3)
df = DataFrame(arr, dtype=str)
expected = DataFrame(arr.astype(str))
tm.assert_frame_equal(df, expected)
