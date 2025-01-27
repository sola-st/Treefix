# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
if dtype:
    dtype = np_utils.result_type(dtype)
start = np_array_ops.array(start, dtype=dtype)
stop = np_array_ops.array(stop, dtype=dtype)
if num < 0:
    raise ValueError(
        'Argument `num` (number of samples) must be a non-negative integer. '
        f'Received: num={num}')
step = ops.convert_to_tensor(np.nan)
if endpoint:
    result = math_ops.linspace(start, stop, num, axis=axis)
    if num > 1:
        step = (stop - start) / (num - 1)
else:
    # math_ops.linspace does not support endpoint=False so we manually handle it
    # here.
    if num > 0:
        step = ((stop - start) / num)
    if num > 1:
        new_stop = math_ops.cast(stop, step.dtype) - step
        start = math_ops.cast(start, new_stop.dtype)
        result = math_ops.linspace(start, new_stop, num, axis=axis)
    else:
        result = math_ops.linspace(start, stop, num, axis=axis)
if dtype:
    if dtype.is_integer:
        # Since numpy 1.20, linspace's rounding is towards -inf instead of 0
        result = math_ops.floor(result)
    result = math_ops.cast(result, dtype)
if retstep:
    exit((result, step))
else:
    exit(result)
