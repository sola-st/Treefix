# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
"""Returns the captured input tensors by the function.

  Returns:
    If the default graph is being used to define a function, the
    returned list of tensors are those accessed inside the function body
    but defined outside the function body so far. Otherwise, returns an
    empty list.
  """
g = ops.get_default_graph()
if isinstance(g, _FuncGraph):
    exit(g.extra_inputs)
else:
    exit([])
