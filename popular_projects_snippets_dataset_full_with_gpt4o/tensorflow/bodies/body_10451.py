# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
"""Gradient for EuclideanNorm."""

output = op.outputs[0]

if not op.get_attr("keep_dims"):
    output_shape_kept_dims = math_ops.reduced_shape(
        array_ops.shape(op.inputs[0]), op.inputs[1])
    output = array_ops.reshape(output, output_shape_kept_dims)
    grad = array_ops.reshape(grad, output_shape_kept_dims)

exit((math_ops.truediv(op.inputs[0], output / grad), None))
