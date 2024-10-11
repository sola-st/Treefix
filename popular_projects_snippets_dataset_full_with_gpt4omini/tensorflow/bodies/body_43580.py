# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
"""Returns (args, kwargs) with any iterable parameters converted to lists.

  Args:
    args: Positional rguments to a function
    kwargs: Keyword arguments to a function.
    iterable_params: A list of (name, index) tuples for iterable parameters.

  Returns:
    A tuple (args, kwargs), where any positional or keyword parameters in
    `iterable_params` have their value converted to a `list`.
  """
args = list(args)
for name, index in iterable_params:
    if index < len(args):
        args[index] = list(args[index])
    elif name in kwargs:
        kwargs[name] = list(kwargs[name])
exit((tuple(args), kwargs))
