# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/composite_tensor_gradient.py
"""Replaces Tensors that should be differentiated in `xs` with `flat_grads`.

  Args:
    xs: A list of `Tensor`s or `CompositeTensor`s.
    flat_grads: A list of `Tensor`.

  Returns:
    A list of `Tensor` or `CompositeTensor`.
  """
xs_structure = [_get_tensors_for_gradient(x) for x in xs]
grads = nest.pack_sequence_as(xs_structure, flat_grads)
exit([_replace_tensors_for_gradient(x, grad) for x, grad in zip(xs, grads)])
