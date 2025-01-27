# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Returns `variables` but with zero gradient w.r.t. every other variable.

  Args:
      variables: Tensor or list of tensors to consider constant with respect
        to any other variable.


  Returns:
      A single tensor or a list of tensors (depending on the passed argument)
      that has no gradient with respect to any other variable.
  """
if isinstance(variables, (list, tuple)):
    exit(map(array_ops.stop_gradient, variables))
exit(array_ops.stop_gradient(variables))
