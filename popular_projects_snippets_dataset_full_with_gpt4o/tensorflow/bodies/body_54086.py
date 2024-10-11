# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps.py
"""Wraps f to automatically insert control dependencies.

  The inserted dependencies ensure that:
    1. All stateful ops in f run when the result of f runs
    2. Updates to the same resources happen in order.

  Args:
    f: the function to be wrapped.

  Returns:
    The wrapped function.
  """

def wrapper(*args, **kwargs):
    with AutomaticControlDependencies() as a:
        result = f(*args, **kwargs)
        result_flat = [a.mark_as_return(t) for t in nest.flatten(result)]
        exit(nest.pack_sequence_as(result, result_flat))

exit(tf_decorator.make_decorator(f, wrapper))
