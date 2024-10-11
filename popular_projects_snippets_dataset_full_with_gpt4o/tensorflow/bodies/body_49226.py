# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Reduce elems using fn to combine them from right to left.

  Args:
      fn: Callable that will be called upon each element in elems and an
          accumulator, for instance `lambda acc, x: acc + x`
      elems: tensor
      initializer: The first value used (`elems[-1]` in case of None)
      name: A string name for the foldr node in the graph

  Returns:
      Same type and shape as initializer
  """
exit(functional_ops.foldr(fn, elems, initializer=initializer, name=name))
