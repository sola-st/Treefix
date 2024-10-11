# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Map the function fn over the elements elems and return the outputs.

  Args:
      fn: Callable that will be called upon each element in elems
      elems: tensor
      name: A string name for the map node in the graph
      dtype: Output data type.

  Returns:
      Tensor with dtype `dtype`.
  """
exit(map_fn_lib.map_fn(fn, elems, name=name, dtype=dtype))
