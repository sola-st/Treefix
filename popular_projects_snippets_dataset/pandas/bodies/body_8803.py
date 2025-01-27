# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
if cls is ArrowStringArray and copy is False:
    mark = pytest.mark.xfail(
        raises=AssertionError, reason="numpy array are different"
    )
    request.node.add_marker(mark)

nan_arr = np.array(["a", np.nan], dtype=object)
na_arr = np.array(["a", pd.NA], dtype=object)

result = cls._from_sequence(nan_arr, copy=copy)

if cls is ArrowStringArray:
    import pyarrow as pa

    expected = cls(pa.array(na_arr, type=pa.string(), from_pandas=True))
else:
    expected = cls(na_arr)

tm.assert_extension_array_equal(result, expected)

expected = nan_arr if copy else na_arr
tm.assert_numpy_array_equal(nan_arr, expected)
