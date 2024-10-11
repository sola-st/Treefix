# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_3d_test.py
"""Verifies the output values of the pooling function.

    Args:
      pool_func: Function to be called: co.MaxPool, co.AvgPool.
      input_sizes: Input tensor dimensions.
      window: Tuple of kernel dims: planes, rows, cols.
      strides: Tuple of strides for dims: planes, rows, cols.
      padding: Padding type.
      expected: An array containing the expected operation outputs.
    """
total_size = 1
for s in input_sizes:
    total_size *= s
# Initializes the input tensor with array containing incrementing
# numbers from 1.
x = np.arange(1.0, total_size + 1, dtype=np.float32)
x = x.reshape(input_sizes)
with self.session() as sess, self.test_scope():
    inputs = array_ops.placeholder(dtypes.float32)
    t = pool_func(
        inputs,
        ksize=[1] + window + [1],
        strides=[1] + strides + [1],
        padding=padding)
    vals = sess.run(t, {inputs: x})
# Verifies values.
actual = vals.flatten()
self.assertAllClose(expected, actual)
