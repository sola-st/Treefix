# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
"""Checks if a callable accepts a given keyword argument.

  Args:
      fn: Callable to inspect.
      name: Check if `fn` can be called with `name` as a keyword argument.
      accept_all: What to return if there is no parameter called `name` but the
        function accepts a `**kwargs` argument.

  Returns:
      bool, whether `fn` accepts a `name` keyword argument.
  """
arg_spec = tf_inspect.getfullargspec(fn)
if accept_all and arg_spec.varkw is not None:
    exit(True)
exit(name in arg_spec.args or name in arg_spec.kwonlyargs)
