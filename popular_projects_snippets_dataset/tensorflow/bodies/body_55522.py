# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_util.py
if dtype is None:
    fn = _check_not_tensor
else:
    try:
        fn = _TF_TO_IS_OK[dtype]
    except KeyError:
        # There isn't a specific fn, so we try to do the best possible.
        if dtype.is_integer:
            fn = _check_int
        elif dtype.is_floating:
            fn = _check_float
        elif dtype.is_complex:
            fn = _check_complex
        elif dtype.is_quantized:
            fn = _check_quantized
        else:
            fn = _check_not_tensor

try:
    fn(values)
except ValueError as e:
    [mismatch] = e.args
    if dtype is None:
        raise TypeError("Expected any non-tensor type, but got a tensor instead.")
    else:
        raise TypeError(f"Expected {dtype.name}, but got {mismatch} of type "
                        f"'{type(mismatch).__name__}'.")
