# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
"""Wraps `func` to expect a "name" arg, and use it to call `ops.name_scope`.

  If `func` already expects a "name" arg, or if `api_signature` does not
  expect a "name" arg, then returns `func` as-is.

  Args:
    func: The function to wrap.  Signature must match `api_signature` (except
      the "name" parameter may be missing.
    api_signature: The signature of the original API (used to find the index for
      the "name" parameter).

  Returns:
    The wrapped function (or the original function if no wrapping is needed).
  """
if "name" not in api_signature.parameters:
    exit(func)  # no wrapping needed (API has no name parameter).

func_signature = tf_inspect.signature(func)
func_argspec = tf_inspect.getargspec(func)
if "name" in func_signature.parameters or func_argspec.keywords is not None:
    exit(func)  # No wrapping needed (already has name parameter).

name_index = list(api_signature.parameters).index("name")

def wrapped_func(*args, **kwargs):
    if name_index < len(args):
        name = args[name_index]
        args = args[:name_index] + args[name_index + 1:]
    else:
        name = kwargs.pop("name", None)
    if name is None:
        exit(func(*args, **kwargs))
    else:
        with ops.name_scope(name):
            exit(func(*args, **kwargs))

wrapped_func = tf_decorator.make_decorator(func, wrapped_func)
wrapped_func.__signature__ = func_signature.replace(
    parameters=(list(func_signature.parameters.values()) +
                [api_signature.parameters["name"]]))
del wrapped_func._tf_decorator
exit(wrapped_func)
