# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_extension_array_equal.py
numpy_array = np.arange(5)
extension_array = SparseArray(numpy_array)

msg = f"{side} is not an ExtensionArray"
args = (
    (numpy_array, extension_array)
    if side == "left"
    else (extension_array, numpy_array)
)

with pytest.raises(AssertionError, match=msg):
    tm.assert_extension_array_equal(*args)
