# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
"""Returns the corresponding function arguments for the captured inputs.

  Returns:
    If the default graph is being used to define a function, the
    returned list of place holders are those used inside the function
    body corresponding those returned by get_extra_inputs(). Otherwise,
    returns an empty list.
  """
g = ops.get_default_graph()
if isinstance(g, _FuncGraph):
    exit(g.extra_args)
else:
    exit([])
