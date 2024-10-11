# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
"""Verifies the output values of the pooling function.

    Args:
      pool_func: Function to be called, co.MaxPool, co.AvgPool,
        or the Lua version.
      input_sizes: Input tensor dimensions.
      ksize: The kernel size dimensions
      strides: The stride dimensions
      padding: Padding type.
      data_format: The data format we use to run the pooling operation.
      data_type: The data type to use to run the pooling operation.
      expected: An array containing the expected operation outputs.
      use_gpu: Whether we are running on GPU.
      v2: Whether to use v2 version.
      use_negative_input: If the input values should be negative.
    """
# Check that this test is compatible with the hardware we have.  (Really
# this should be done in GetTestConfigsDicts(), but when that runs, we
# haven't initialized enough of TF to know what our hardware is!)
if use_gpu and not test.is_gpu_available():
    self.skipTest("No GPU is available.")
if use_gpu and data_type == dtypes.float64 and test.is_built_with_rocm():
    self.skipTest("ROCm pooling ops don't support float64.")
if use_gpu and data_format == "NCHW_VECT_C" and not test.is_gpu_available(
    cuda_only=True, min_cuda_compute_capability=(6, 1)):
    self.skipTest("NCHW_VECT_C requires sm61+.")

if v2 and data_format != "NHWC":
    self.skipTest("v2 not supported for %s" % data_format)
if v2 and not isinstance(padding, str):
    self.skipTest("non-constant ksize/strides requires nonexplicit padding")
if data_format == "NCHW_VECT_C":
    if data_type != dtypes.float32:
        self.skipTest("quantization to qint8 not implemented for %r" %
                      data_type)
    if input_sizes[-1] % 4 != 0:
        self.skipTest("Skipping test for depth %d" % input_sizes[-1])

total_size = 1
for s in input_sizes:
    total_size *= s
tf_logging.info("Running %s test. %r %r %d %r %r %r %s", data_format, v2,
                input_sizes, total_size, pool_func, ksize, strides,
                data_type)
# Initializes the input tensor with array containing incrementing
# numbers from 1, wrapping round to -127 after 127 to support int8.
y = -1 if use_negative_input else 1
x = [(((f + 128) % 255) - 127)*y for f in range(total_size)]
with self.cached_session(use_gpu=use_gpu):
    t = constant_op.constant(x, shape=input_sizes, dtype=data_type)
    if data_format in ("NCHW", "NCHW_VECT_C", "NCW"):
        if data_format == "NCHW_VECT_C":
            t = test_util.NHWCToNCHW_VECT_C(t)
            t, _, _ = gen_array_ops.quantize_v2(t, -128.0, 127.0, dtypes.qint8)
        else:
            t = test_util.NHWCToNCHW(t)
        ksize = test_util.NHWCToNCHW(ksize)
        strides = test_util.NHWCToNCHW(strides)
        if isinstance(padding, list):
            padding = test_util.NHWCToNCHW(padding)
    ksize_placeholder = array_ops.placeholder(dtypes.int32, shape=[4])
    strides_placeholder = array_ops.placeholder(dtypes.int32, shape=[4])
    if v2:
        t = pool_func(
            t,
            ksize=ksize_placeholder,
            strides=strides_placeholder,
            padding=padding,
            data_format=data_format)
    else:
        t = pool_func(
            t,
            ksize=ksize,
            strides=strides,
            padding=padding,
            data_format=data_format)
    if data_format == "NCHW_VECT_C":
        t = gen_array_ops.dequantize(t, -128, 127)
        t = test_util.NCHW_VECT_CToNHWC(t)
    elif data_format == "NCHW":
        t = test_util.NCHWToNHWC(t)
    if v2:
        actual = t.eval(feed_dict={
            ksize_placeholder: ksize,
            strides_placeholder: strides
        })
    else:
        actual = self.evaluate(t)
        self.assertShapeEqual(actual, t)
    self.assertAllCloseAccordingToType(expected, actual.flatten())
