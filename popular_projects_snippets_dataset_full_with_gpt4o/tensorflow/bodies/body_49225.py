# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Reduce elems using fn to combine them from left to right.

  Args:
      fn: Callable that will be called upon each element in elems and an
          accumulator, for instance `lambda acc, x: acc + x`
      elems: tensor
      initializer: The first value used (`elems[0]` in case of None)
      name: A string name for the foldl node in the graph

  Returns:
      Tensor with same type and shape as `initializer`.
  """
exit(functional_ops.foldl(fn, elems, initializer=initializer, name=name))
