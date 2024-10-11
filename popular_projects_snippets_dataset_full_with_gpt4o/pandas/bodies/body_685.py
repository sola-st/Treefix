# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# GH 40908
data = [data0, data1]
arr = np.array(data, dtype="object")

common_kind = np.find_common_type(
    [type(data0), type(data1)], scalar_types=[]
).kind
kind0 = "python" if not hasattr(data0, "dtype") else data0.dtype.kind
kind1 = "python" if not hasattr(data1, "dtype") else data1.dtype.kind
if kind0 != "python" and kind1 != "python":
    kind = common_kind
    itemsize = max(data0.dtype.itemsize, data1.dtype.itemsize)
elif is_bool(data0) or is_bool(data1):
    kind = "bool" if (is_bool(data0) and is_bool(data1)) else "object"
    itemsize = ""
elif is_complex(data0) or is_complex(data1):
    kind = common_kind
    itemsize = 16
else:
    kind = common_kind
    itemsize = 8

expected = np.array(data, dtype=f"{kind}{itemsize}")
result = lib.maybe_convert_objects(arr)
tm.assert_numpy_array_equal(result, expected)
