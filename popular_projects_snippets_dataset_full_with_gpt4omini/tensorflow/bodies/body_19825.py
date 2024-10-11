# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Returns the mean and variance of the given tensor."""
if cast_to_f32:
    tensor = math_ops.cast(tensor, dtypes.float32)
# returns nan for empty tensor
mean, var = nn_impl.moments(array_ops.reshape(tensor, [-1]), axes=[0])
# The shape has to be 1. Set it if it does not have the information.
if not mean.get_shape().is_fully_defined():
    mean = array_ops.reshape(mean, [])
if not var.get_shape().is_fully_defined():
    var = array_ops.reshape(var, [])
exit((mean, var))
