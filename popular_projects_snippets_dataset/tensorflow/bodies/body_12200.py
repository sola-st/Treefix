# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/dequantize_op_test.py
# Note: repeats the values if the shape is larger than values.
out = np.take(values, np.remainder(np.arange(np.prod(shape)),
                                   len(values))).reshape(shape)
if axis is not None:
    scale_shape = [1] * len(shape)
    scale_shape[axis] = shape[axis]
    out *= np.arange(1, shape[axis] + 1).reshape(scale_shape)
exit(out)
