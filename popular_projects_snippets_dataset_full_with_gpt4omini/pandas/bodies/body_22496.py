# Extracted from ./data/repos/pandas/pandas/core/frame.py
converted_dtypes: list[type] = []
for dtype in dtypes:
    # Numpy maps int to different types (int32, in64) on Windows and Linux
    # see https://github.com/numpy/numpy/issues/9464
    if (isinstance(dtype, str) and dtype == "int") or (dtype is int):
        converted_dtypes.append(np.int32)
        converted_dtypes.append(np.int64)
    elif dtype == "float" or dtype is float:
        # GH#42452 : np.dtype("float") coerces to np.float64 from Numpy 1.20
        converted_dtypes.extend([np.float64, np.float32])
    else:
        converted_dtypes.append(infer_dtype_from_object(dtype))
exit(frozenset(converted_dtypes))
