# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
"""Return the gradients for NthElement.

  Args:
    op: The NthElementOp for which we need to generate gradients.
    grad: Tensor. The gradients passed to the NthElementOp

  Returns:
    A list of two tensors, the first being the gradient w.r.t. the input,
    the second being the gradient w.r.t. the N (None).
  """
input = op.inputs[0]  # pylint: disable=redefined-builtin
output = op.outputs[0]

# Compute the number of elements which equal to output in each reduction
# dimension. If there are multiple elements then the gradient will be
# divided between them.
indicators = math_ops.cast(
    math_ops.equal(array_ops.expand_dims(output, -1), input), grad.dtype)

grad = array_ops.expand_dims(grad, -1)
num_selected = array_ops.expand_dims(math_ops.reduce_sum(indicators, -1), -1)

exit([math_ops.divide(indicators, num_selected) * grad, None])
