# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
"""Verifies the gradients of the max or avg pooling function.

    Args:
      pool_func: Function to be called, co.MaxPool, co.AvgPool,
        or the Lua version.
      input_sizes: Input tensor dimensions.
      output_sizes: Output tensor dimensions.
      window_rows: kernel size in row dim
      window_cols: kernel size in col dim
      row_stride: Row Stride.
      col_stride: Col Stride.
      padding: Padding type.
      data_format: Data format.
      use_gpu: whether we are running on GPU
      x_init_value: Values to be passed to the gradient checker.
    """
assert input_sizes[0] == output_sizes[0]
assert input_sizes[3] == output_sizes[3]
total_size = 1
for s in input_sizes:
    total_size *= s
# Initializes the input tensor with array containing incrementing
# numbers from 1.
x = [f * 1.0 for f in range(1, total_size + 1)]
with self.cached_session(use_gpu=use_gpu):
    input_tensor = constant_op.constant(x, shape=input_sizes, name="input")
    if pool_func == nn_ops.avg_pool:
        func_name = "avg_pool"
        err_tolerance = 1e-4
    else:
        if x_init_value is None:
            x_init_value = np.asfarray(
                np.arange(1, total_size + 1),
                dtype=np.float32).reshape(input_sizes)
        func_name = "max_pool"
        err_tolerance = 1e-3
    if data_format == "NCHW":
        ksize = [1, 1, window_rows, window_cols]
        strides = [1, 1, row_stride, col_stride]
        if isinstance(padding, list):
            padding = test_util.NHWCToNCHW(padding)
        t = test_util.NHWCToNCHW(input_tensor)
    else:
        ksize = [1, window_rows, window_cols, 1]
        strides = [1, row_stride, col_stride, 1]
        t = input_tensor
    t = pool_func(
        t,
        ksize=ksize,
        strides=strides,
        padding=padding,
        data_format=data_format,
        name=func_name)
    if data_format == "NCHW":
        t = test_util.NCHWToNHWC(t)

    err = gradient_checker.compute_gradient_error(
        input_tensor,
        input_sizes,
        t,
        output_sizes,
        x_init_value=x_init_value,
        delta=1e-2)
tf_logging.info("%s gradient error = %.4f" % (func_name, err))
self.assertLess(err, err_tolerance)
