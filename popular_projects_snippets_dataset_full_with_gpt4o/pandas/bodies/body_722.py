# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# see gh-13320
rows = [[1, 2, 3], [4, 5, 6]]

expected = np.array(rows, dtype=object)
out = lib.to_object_array(rows)
tm.assert_numpy_array_equal(out, expected)

expected = np.array(rows, dtype=object)
out = lib.to_object_array(rows, min_width=1)
tm.assert_numpy_array_equal(out, expected)

expected = np.array(
    [[1, 2, 3, None, None], [4, 5, 6, None, None]], dtype=object
)
out = lib.to_object_array(rows, min_width=5)
tm.assert_numpy_array_equal(out, expected)
