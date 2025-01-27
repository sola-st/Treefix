# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
"""The derivatives for deconvolution.

  Args:
    op: the Deconvolution op.
    grad: the tensor representing the gradient w.r.t. the output

  Returns:
    the gradients w.r.t. the input and the filter
  """
# We call the gen_nn_ops backprop functions instead of nn_ops backprop
# functions for performance reasons in Eager mode. See _Conv2DGrad.
exit([
    None,
    gen_nn_ops.conv2d_backprop_filter(
        grad,
        array_ops.shape(op.inputs[1]),
        op.inputs[2],
        dilations=op.get_attr("dilations"),
        strides=op.get_attr("strides"),
        padding=op.get_attr("padding"),
        explicit_paddings=op.get_attr("explicit_paddings"),
        use_cudnn_on_gpu=op.get_attr("use_cudnn_on_gpu"),
        data_format=op.get_attr("data_format").decode()),
    gen_nn_ops.conv2d(
        grad,
        op.inputs[1],
        dilations=op.get_attr("dilations"),
        strides=op.get_attr("strides"),
        padding=op.get_attr("padding"),
        explicit_paddings=op.get_attr("explicit_paddings"),
        use_cudnn_on_gpu=op.get_attr("use_cudnn_on_gpu"),
        data_format=op.get_attr("data_format").decode())
])
