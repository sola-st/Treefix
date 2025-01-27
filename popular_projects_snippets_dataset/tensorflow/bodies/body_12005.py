# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_norm_benchmark.py
"""Build a graph containing a sequence of batch normalizations.

  Args:
    device: string, the device to run on.
    input_shape: shape of the input tensor.
    axes: axes that are to be normalized across.
    num_layers: number of batch normalization layers in the graph.
    mode: "op", "py" or "slow" depending on the implementation.
    scale: scale after normalization.
    train: if true, also run backprop.

  Returns:
    An array of tensors to run()
  """
moment_shape = []
keep_dims = mode == "py" or mode == "slow"
if keep_dims:
    for axis in range(len(input_shape)):
        if axis in axes:
            moment_shape.append(1)
        else:
            moment_shape.append(input_shape[axis])
else:
    for axis in range(len(input_shape)):
        if axis not in axes:
            moment_shape.append(input_shape[axis])
with ops.device("/%s:0" % device):
    tensor = variables.Variable(random_ops.truncated_normal(input_shape))
    for _ in range(num_layers):
        if train:
            mean, variance = nn_impl.moments(tensor, axes, keep_dims=keep_dims)
        else:
            mean = array_ops.zeros(moment_shape)
            variance = array_ops.ones(moment_shape)
        beta = variables.Variable(array_ops.zeros(moment_shape))
        gamma = variables.Variable(constant_op.constant(1.0, shape=moment_shape))
        if mode == "py":
            tensor = batch_norm_py(tensor, mean, variance, beta, gamma, scale)
        elif mode == "op":
            tensor = batch_norm_op(tensor, mean, variance, beta, gamma, scale)
        elif mode == "slow":
            tensor = batch_norm_slow(tensor, mean, variance, beta, gamma, scale)
    if train:
        exit(gradients_impl.gradients([tensor], variables.trainable_variables()))
    else:
        exit([tensor])
