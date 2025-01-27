# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/depthwise_conv_op_base.py
"""Verifies the output values of the convolution function.

    Args:
      tensor_in_sizes: Input tensor dimensions in [batch, input_rows,
        input_cols, input_depth].
      filter_in_sizes: Filter tensor dimensions in [filter_rows, filter_cols,
        input_depth, depth_multiplier].
      stride: Stride.
      padding: Padding type.
      data_type: The data type to use.
      use_gpu: Whether to use GPU.
      grouped_conv: Whether to use cuDNN 7's grouped convolution.
      data_format: The data_format of the input. "NHWC" or "NCHW".
      dilations: A list of 2 elements, representing the dilations.
      tolerance: The absolute and relative tolarance when verifying the output.
    """
input_size = 1
filter_size = 1
for s in tensor_in_sizes:
    input_size *= s
for s in filter_in_sizes:
    filter_size *= s
# Initializes the input and filter tensor with numbers incrementing to 1.0.
x1 = [f * 1.0 / input_size for f in range(1, input_size + 1)]
x1 = np.array(x1).reshape(tensor_in_sizes)
x2 = [f * 1.0 / filter_size for f in range(1, filter_size + 1)]
x2 = np.array(x2).reshape(filter_in_sizes)
# Compute reference result
strides = [1, stride, stride, 1]
if isinstance(padding, list):
    padding = [(0, 0)] + padding + [(0, 0)]
np_result = _DepthwiseConv2dNumpy(x1, x2, strides, padding, "NHWC",
                                  dilations)

ops.reset_default_graph()
graph = ops.get_default_graph()
with self.session(graph=graph, use_gpu=use_gpu) as sess:
    tolerance = tolerance or {
        dtypes.float16: 4e-2,
        dtypes.float32: 1e-5,
        dtypes.float64: 1e-12,
        dtypes.bfloat16: 1e-2,
    }[data_type]

    t1 = constant_op.constant(x1, shape=tensor_in_sizes, dtype=data_type)
    t2 = constant_op.constant(x2, shape=filter_in_sizes, dtype=data_type)

    if data_format == "NCHW":
        # Transpose from NHWC input to NCHW
        # Ex. [4, 5, 5, 48] to [4, 48, 5, 5]
        t1 = array_ops.transpose(t1, [0, 3, 1, 2])
        strides = [1, 1, stride, stride]
        if isinstance(padding, list):
            padding = [padding[0], padding[3], padding[1], padding[2]]

      # depthwise_conv2d_native does not support dilations except on TPUs.
    if dilations is None:
        with sess.graph._kernel_label_map(  # pylint: disable=protected-access
            {"DepthwiseConv2dNative": "cudnn_grouped_convolution"}
            if grouped_conv else {}):
            conv_native = nn_ops.depthwise_conv2d_native(
                t1, t2, strides=strides, data_format=data_format, padding=padding)

        if data_format == "NCHW":
            # Transpose back from NCHW to NHWC
            conv_native = array_ops.transpose(conv_native, [0, 2, 3, 1])

        try:
            # The Numpy array from calling depthwise_conv2d_native
            native_result = self.evaluate(conv_native)
        except errors.InvalidArgumentError as e:
            # Grouped convolution kernel is only registered for cuDNN 7. Silently
            # return when we are running on an earlier version or without GPU.
            if ("No OpKernel was registered to support Op "
                "'DepthwiseConv2dNative'") in e.message:
                tf_logging.warn("Skipping grouped convolution test")
                exit()
            raise e

    conv_interface = nn_impl.depthwise_conv2d(
        t1,
        t2,
        strides=strides,
        padding=padding,
        data_format=data_format,
        dilations=dilations)
    if data_format == "NCHW":
        # Transpose back from NCHW to NHWC
        conv_interface = array_ops.transpose(conv_interface, [0, 2, 3, 1])

    # The Numpy array from calling depthwise_conv2d
    interface_result = self.evaluate(conv_interface)

if dilations is None:
    self.assertAllClose(
        native_result, np_result, atol=tolerance, rtol=tolerance)
self.assertAllClose(
    interface_result, np_result, atol=tolerance, rtol=tolerance)
