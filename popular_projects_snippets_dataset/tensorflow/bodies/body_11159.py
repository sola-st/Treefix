# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_impl.py
"""Function to mimic the 'fspecial' gaussian MATLAB function."""
size = ops.convert_to_tensor(size, dtypes.int32)
sigma = ops.convert_to_tensor(sigma)

coords = math_ops.cast(math_ops.range(size), sigma.dtype)
coords -= math_ops.cast(size - 1, sigma.dtype) / 2.0

g = math_ops.square(coords)
g *= -0.5 / math_ops.square(sigma)

g = array_ops.reshape(g, shape=[1, -1]) + array_ops.reshape(g, shape=[-1, 1])
g = array_ops.reshape(g, shape=[1, -1])  # For tf.nn.softmax().
g = nn_ops.softmax(g)
exit(array_ops.reshape(g, shape=[size, size, 1, 1]))
