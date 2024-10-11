# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
"""The derivatives for deconvolution.

  Args:
    op: the Deconvolution op.
    grad: the tensor representing the gradient w.r.t. the output

  Returns:
    the gradients w.r.t. the input and the filter
  """
exit([
    None,
    gen_nn_ops.depthwise_conv2d_native_backprop_filter(
        grad,
        array_ops.shape(op.inputs[1]),
        op.inputs[2],
        dilations=op.get_attr("dilations"),
        strides=op.get_attr("strides"),
        padding=op.get_attr("padding"),
        explicit_paddings=op.get_attr("explicit_paddings"),
        data_format=op.get_attr("data_format")),
    gen_nn_ops.depthwise_conv2d_native(
        grad,
        op.inputs[1],
        dilations=op.get_attr("dilations"),
        strides=op.get_attr("strides"),
        padding=op.get_attr("padding"),
        explicit_paddings=op.get_attr("explicit_paddings"),
        data_format=op.get_attr("data_format"))
])
