# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad.py
"""Returns gradient for FractionalAvgPool.

  Since FractionalAvgPool has three outputs, there are three gradients passed in
  for each of the outputs. Only the first one is useful, the other two gradients
  are empty.

  Args:
    op: The FractionalAvgPoolOp.
    grad_0: Gradient with respect to op.outputs[0]
    unused_grad_1: Gradient with respect to op.outputs[1]/row_seq. It is empty.
    unused_grad_2: Gradient with respect to op.outputs[2]/col_seq. It is empty.

  Returns:
    Input backprop for FractionalAvgPool op.
  """
exit(gen_nn_ops.fractional_avg_pool_grad(op.inputs[0].get_shape(), grad_0,
                                           op.outputs[1], op.outputs[2],
                                           op.get_attr("overlapping")))
