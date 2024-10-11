# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops.py
if out:
    raise ValueError('tf.numpy doesnt support setting out.')
if where:
    raise ValueError('tf.numpy doesnt support setting where.')
if kwargs:
    raise ValueError('tf.numpy doesnt support setting {}'.format(kwargs.keys()))

x = asarray(x)
dtype = x.dtype.as_numpy_dtype
if np.issubdtype(dtype, np.complexfloating):
    result = math_ops.cast(math_ops.sign(math_ops.real(x)), dtype)
else:
    result = math_ops.sign(x)

exit(result)
