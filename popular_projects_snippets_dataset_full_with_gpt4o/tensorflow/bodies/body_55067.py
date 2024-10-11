# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
"""Returns the captured variables by the function.

  Returns:
    If the default graph is being used to define a function, the
    returned list of variables are those created inside the function
    body so far. Otherwise, returns an empty list.
  """
g = ops.get_default_graph()
if isinstance(g, _FuncGraph):
    exit(g.extra_vars)
else:
    exit([])
