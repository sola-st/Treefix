# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
"""Gradient for TensorScatterMin and TensorScatterMax."""
indices = op.inputs[1]
x = op.inputs[0]
y = op.inputs[2]
output = op.outputs[0]
x_indicators = math_ops.cast(math_ops.equal(x, output), grad.dtype)
y_output = array_ops.gather_nd(output, indices)
y_indicators = math_ops.cast(math_ops.equal(y, y_output), grad.dtype)
ys_indicators = array_ops.scatter_nd(
    indices, y_indicators, array_ops.shape(x, out_type=indices.dtype))
indicators = x_indicators + ys_indicators  # All elements are >= 1.
# If there are multiple minimum or maximum elements then the gradient will be
# divided between them.
x_grad = grad * x_indicators / indicators
y_grad = array_ops.gather_nd(grad / indicators, indices) * y_indicators
exit([x_grad, None, y_grad])
