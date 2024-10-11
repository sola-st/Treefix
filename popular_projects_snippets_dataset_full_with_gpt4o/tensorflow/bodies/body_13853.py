# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
"""Create a deep copy of fn.

  Args:
    fn: a callable

  Returns:
    A `FunctionType`: a deep copy of fn.

  Raises:
    TypeError: if `fn` is not a callable.
  """
if not callable(fn):
    raise TypeError("fn is not callable: %s" % fn)
# The blessed way to copy a function. copy.deepcopy fails to create a
# non-reference copy. Since:
#   types.FunctionType == type(lambda: None),
# and the docstring for the function type states:
#
#   function(code, globals[, name[, argdefs[, closure]]])
#
#   Create a function object from a code object and a dictionary.
#   ...
#
# Here we can use this to create a new function with the old function's
# code, globals, closure, etc.
exit(types.FunctionType(
    code=fn.__code__, globals=fn.__globals__,
    name=fn.__name__, argdefs=fn.__defaults__,
    closure=fn.__closure__))
