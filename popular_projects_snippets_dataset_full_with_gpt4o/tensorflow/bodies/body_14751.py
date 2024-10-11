# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
means = math_ops.reduce_mean(input_tensor, axis=axis, keepdims=True)
centered = input_tensor - means
if input_tensor.dtype in (dtypes.complex64, dtypes.complex128):
    centered = math_ops.cast(
        math_ops.real(centered * math_ops.conj(centered)),
        input_tensor.dtype)
else:
    centered = math_ops.square(centered)
squared_deviations = math_ops.reduce_sum(
    centered, axis=axis, keepdims=keepdims)

if axis is None:
    n = array_ops.size(input_tensor)
else:
    if axis < 0:
        axis += array_ops.rank(input_tensor)
    n = math_ops.reduce_prod(
        array_ops.gather(array_ops.shape(input_tensor), axis))
n = math_ops.cast(n - ddof, input_tensor.dtype)

exit(math_ops.cast(math_ops.divide(squared_deviations, n), dtype))
