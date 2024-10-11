# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/pooling_ops_test.py
"""Verifies the output values of the pooling function.

    Args:
      pool_func: Function to be called, currently only co.MaxPool.
      input_sizes: Input tensor dimensions.
      ksize: The kernel size dimensions
      strides: The stride dimensions
      padding: Padding type.
      data_format: The data format we use to run the pooling operation.
      expected: An array containing the expected operation outputs.
    """
total_size = np.prod(input_sizes)
# Initializes the input tensor with array containing incrementing
# numbers from 1.
x = np.array([f * 1.0 for f in range(1, total_size + 1)], dtype=np.float32)
x = x.reshape(input_sizes)
with self.session() as sess:
    with self.test_scope():
        inputs = array_ops.placeholder(dtypes.float32)
        t = inputs
        if data_format == "NCHW":
            t = NHWCToNCHW(t)
            ksize = NHWCToNCHW(ksize)
            strides = NHWCToNCHW(strides)
        t = pool_func(t,
                      ksize=ksize,
                      strides=strides,
                      padding=padding,
                      data_format=data_format)
        if data_format == "NCHW":
            t = NCHWToNHWC(t)
    actual = sess.run(t, {inputs: x})
    self.assertAllClose(expected, actual.flatten(), rtol=1e-5, atol=1e-6)
