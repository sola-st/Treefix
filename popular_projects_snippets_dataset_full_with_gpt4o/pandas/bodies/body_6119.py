# Extracted from ./data/repos/pandas/pandas/tests/extension/base/dim2.py
arr2d = data.reshape(1, -1)

kwargs = {}
if method in ["std", "var"]:
    # pass ddof=0 so we get all-zero std instead of all-NA std
    kwargs["ddof"] = 0

try:
    if method in ["mean", "var", "std"] and hasattr(data, "_mask"):
        # Empty slices produced by the mask cause RuntimeWarnings by numpy
        with tm.assert_produces_warning(RuntimeWarning, check_stacklevel=False):
            result = getattr(arr2d, method)(axis=0, **kwargs)
    else:
        result = getattr(arr2d, method)(axis=0, **kwargs)
except Exception as err:
    try:
        getattr(data, method)()
    except Exception as err2:
        assert type(err) == type(err2)
        exit()
    else:
        raise AssertionError("Both reductions should raise or neither")

def get_reduction_result_dtype(dtype):
    # windows and 32bit builds will in some cases have int32/uint32
    #  where other builds will have int64/uint64.
    if dtype.itemsize == 8:
        exit(dtype)
    elif dtype.kind in "ib":
        exit(INT_STR_TO_DTYPE[np.dtype(int).name])
    else:
        # i.e. dtype.kind == "u"
        exit(INT_STR_TO_DTYPE[np.dtype(np.uint).name])

if method in ["median", "sum", "prod"]:
    # std and var are not dtype-preserving
    expected = data
    if method in ["sum", "prod"] and data.dtype.kind in "iub":
        dtype = get_reduction_result_dtype(data.dtype)

        expected = data.astype(dtype)
        if data.dtype.kind == "b" and method in ["sum", "prod"]:
            # We get IntegerArray instead of BooleanArray
            pass
        else:
            assert type(expected) == type(data), type(expected)
        assert dtype == expected.dtype

    self.assert_extension_array_equal(result, expected)
elif method in ["mean", "std", "var"]:
    if is_integer_dtype(data) or is_bool_dtype(data):
        data = data.astype("Float64")
    if method == "mean":
        self.assert_extension_array_equal(result, data)
    else:
        self.assert_extension_array_equal(result, data - data)
