# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
arr = arr1d
if box is None:
    pass
elif box == "index":
    # Test the equivalent Index.searchsorted method while we're here
    arr = self.index_cls(arr)
else:
    # Test the equivalent Series.searchsorted method while we're here
    arr = pd.Series(arr)

# scalar
result = arr.searchsorted(str(arr[1]))
assert result == 1

result = arr.searchsorted(str(arr[2]), side="right")
assert result == 3

result = arr.searchsorted([str(x) for x in arr[1:3]])
expected = np.array([1, 2], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)

with pytest.raises(
    TypeError,
    match=re.escape(
        f"value should be a '{arr1d._scalar_type.__name__}', 'NaT', "
        "or array of those. Got 'str' instead."
    ),
):
    arr.searchsorted("foo")

arr_type = "StringArray" if string_storage == "python" else "ArrowStringArray"

with pd.option_context("string_storage", string_storage):
    with pytest.raises(
        TypeError,
        match=re.escape(
            f"value should be a '{arr1d._scalar_type.__name__}', 'NaT', "
            f"or array of those. Got '{arr_type}' instead."
        ),
    ):
        arr.searchsorted([str(arr[1]), "baz"])
