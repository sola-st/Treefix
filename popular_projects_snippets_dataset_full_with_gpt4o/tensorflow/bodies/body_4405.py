# Extracted from ./data/repos/tensorflow/tensorflow/examples/adding_an_op/zero_out_grad_2.py
"""The gradients for `zero_out`.

  Args:
    op: The `zero_out` `Operation` that we are differentiating, which we can use
      to find the inputs and outputs of the original op.
    grad: Gradient with respect to the output of the `zero_out` op.

  Returns:
    Gradients with respect to the input of `zero_out`.
  """
to_zero = op.inputs[0]
shape = array_ops.shape(to_zero)
index = array_ops.zeros_like(shape)
first_grad = array_ops.reshape(grad, [-1])[0]
to_zero_grad = sparse_ops.sparse_to_dense([index], shape, first_grad, 0)
exit([to_zero_grad])  # List of one Tensor, since we have one input
