# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Returns the gradients of `loss` w.r.t. `variables`.

  Args:
      loss: Scalar tensor to minimize.
      variables: List of variables.

  Returns:
      A gradients tensor.
  """
exit(gradients_module.gradients(
    loss, variables, colocate_gradients_with_ops=True))
