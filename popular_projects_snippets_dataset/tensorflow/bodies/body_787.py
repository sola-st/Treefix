# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/depthwise_conv_op_test.py
"""Verifies the output values of the convolution function.

    Args:
      tensor_in_sizes: Input tensor dimensions in [batch, input_rows,
        input_cols, input_depth].
      filter_in_sizes: Filter tensor dimensions in [filter_rows, filter_cols,
        input_depth, depth_multiplier].
      stride: Stride.
      dilation: Dilation.
      padding: Padding type.
      data_type: The data type to use.
      data_format: The data_format of the input. "NHWC" or "NCHW".
    """
total_size_1 = 1
total_size_2 = 1
for s in tensor_in_sizes:
    total_size_1 *= s
for s in filter_in_sizes:
    total_size_2 *= s
# Initializes the input and filter tensor with numbers incrementing from 1.
x1 = np.array([f * 1.0 for f in range(1, total_size_1 + 1)],
              dtype=data_type).reshape(tensor_in_sizes)
x2 = np.array([f * 1.0 for f in range(1, total_size_2 + 1)],
              dtype=data_type).reshape(filter_in_sizes)
with self.session() as sess:
    if data_type == np.float32:
        # TODO(b/64210055): Tolerance for TPU is high.
        tolerance = 1e-2
    else:
        self.assertEqual(data_type, np.float64)
        tolerance = 1e-8

    t1 = array_ops.placeholder(shape=tensor_in_sizes, dtype=data_type)
    t2 = array_ops.placeholder(shape=filter_in_sizes, dtype=data_type)

    native_t1 = t1
    strides = [1, stride, stride, 1]
    dilations = [dilation, dilation]
    if data_format == "NCHW":
        # Transpose from NWHC input to NCHW
        # Ex. [4, 5, 5, 48] to [4, 48, 5, 5]
        native_t1 = array_ops.transpose(t1, [0, 3, 1, 2])
        strides = [1, 1, stride, stride]

    with self.test_scope():
        conv_native = nn_impl.depthwise_conv2d(
            native_t1,
            t2,
            strides=strides,
            rate=dilations,
            data_format=data_format,
            padding=padding)

    if data_format == "NCHW":
        # Transpose back from NCHW to NHWC
        conv_native = array_ops.transpose(conv_native, [0, 2, 3, 1])

    with ops.device("CPU"):
        # CPU only support NHWC format
        strides = [1, stride, stride, 1]
        conv_interface = nn_impl.depthwise_conv2d(
            t1, t2, strides=strides, rate=dilations, padding=padding)

    native_result = sess.run(conv_native, {t1: x1, t2: x2})
    interface_result = sess.run(conv_interface, {t1: x1, t2: x2})

print("data_type:", data_type, "max diff = ",
      np.amax(np.absolute(native_result - interface_result)))
self.assertAllClose(
    np.ravel(native_result), np.ravel(interface_result), rtol=tolerance)
