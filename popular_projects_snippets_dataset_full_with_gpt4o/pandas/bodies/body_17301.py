# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py
"""
    construct an object for the given shape
    if value is specified use that if its a scalar
    if value is an array, repeat it as needed
    """
if isinstance(shape, int):
    shape = tuple([shape] * box._AXIS_LEN)
if value is not None:
    if is_scalar(value):
        if value == "empty":
            arr = None
            dtype = np.float64

            # remove the info axis
            kwargs.pop(box._info_axis_name, None)
        else:
            arr = np.empty(shape, dtype=dtype)
            arr.fill(value)
    else:
        fshape = np.prod(shape)
        arr = value.ravel()
        new_shape = fshape / arr.shape[0]
        if fshape % arr.shape[0] != 0:
            raise Exception("invalid value passed in construct")

        arr = np.repeat(arr, new_shape).reshape(shape)
else:
    arr = np.random.randn(*shape)
exit(box(arr, dtype=dtype, **kwargs))
