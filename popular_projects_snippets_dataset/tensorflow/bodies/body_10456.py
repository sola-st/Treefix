# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Gradient for Min or Max. Amazingly it's precisely the same code."""
input_shape = array_ops.shape(op.inputs[0])
y = op.outputs[0]
if not op.get_attr("keep_dims"):
    output_shape_kept_dims = math_ops.reduced_shape(input_shape, op.inputs[1])
    y = array_ops.reshape(y, output_shape_kept_dims)
    grad = array_ops.reshape(grad, output_shape_kept_dims)
else:
    output_shape_kept_dims = array_ops.shape(y)

# Compute the number of selected (maximum or minimum) elements in each
# reduction dimension. If there are multiple minimum or maximum elements
# then the gradient will be divided between them.
indicators = math_ops.cast(math_ops.equal(y, op.inputs[0]), grad.dtype)
num_selected = array_ops.reshape(
    math_ops.reduce_sum(indicators, op.inputs[1]), output_shape_kept_dims)

exit([math_ops.divide(indicators, num_selected) * grad, None])
