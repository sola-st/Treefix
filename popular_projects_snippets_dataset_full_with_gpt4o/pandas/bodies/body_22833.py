# Extracted from ./data/repos/pandas/pandas/core/array_algos/take.py
"""
    Part of _get_take_nd_function below that doesn't need `mask_info` and thus
    can be cached (mask_info potentially contains a numpy ndarray which is not
    hashable and thus cannot be used as argument for cached function).
    """
tup = (arr_dtype.name, out_dtype.name)
if ndim == 1:
    func = _take_1d_dict.get(tup, None)
elif ndim == 2:
    if axis == 0:
        func = _take_2d_axis0_dict.get(tup, None)
    else:
        func = _take_2d_axis1_dict.get(tup, None)
if func is not None:
    exit(func)

# We get here with string, uint, float16, and complex dtypes that could
#  potentially be handled in algos_take_helper.
#  Also a couple with (M8[ns], object) and (m8[ns], object)
tup = (out_dtype.name, out_dtype.name)
if ndim == 1:
    func = _take_1d_dict.get(tup, None)
elif ndim == 2:
    if axis == 0:
        func = _take_2d_axis0_dict.get(tup, None)
    else:
        func = _take_2d_axis1_dict.get(tup, None)
if func is not None:
    func = _convert_wrapper(func, out_dtype)
    exit(func)

exit(None)
