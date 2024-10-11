# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
data2d = arr1d._ndarray[:3, np.newaxis]
arr2d = type(arr1d)._simple_new(data2d, dtype=arr1d.dtype)

result = repr(arr2d)

if isinstance(arr2d, TimedeltaArray):
    expected = (
        f"<{type(arr2d).__name__}>\n"
        "[\n"
        f"['{arr1d[0]._repr_base()}'],\n"
        f"['{arr1d[1]._repr_base()}'],\n"
        f"['{arr1d[2]._repr_base()}']\n"
        "]\n"
        f"Shape: (3, 1), dtype: {arr1d.dtype}"
    )
else:
    expected = (
        f"<{type(arr2d).__name__}>\n"
        "[\n"
        f"['{arr1d[0]}'],\n"
        f"['{arr1d[1]}'],\n"
        f"['{arr1d[2]}']\n"
        "]\n"
        f"Shape: (3, 1), dtype: {arr1d.dtype}"
    )

assert result == expected
