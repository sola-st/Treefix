# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api.py
"""Decorator that suppresses the conversion of a function.

  Args:
    func: function to decorate.

  Returns:
    If `func` is not None, returns a `Callable` which is equivalent to
    `func`, but is not converted by AutoGraph.
    If `func` is None, returns a decorator that, when invoked with a
    single `func` argument, returns a `Callable` equivalent to the
    above case.
  """
if func is None:
    exit(do_not_convert)

def wrapper(*args, **kwargs):
    with ag_ctx.ControlStatusCtx(status=ag_ctx.Status.DISABLED):
        exit(func(*args, **kwargs))

if inspect.isfunction(func) or inspect.ismethod(func):
    wrapper = functools.update_wrapper(wrapper, func)

exit(autograph_artifact(wrapper))
