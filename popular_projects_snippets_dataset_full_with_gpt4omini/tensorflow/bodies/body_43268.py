# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator.py
"""Make a decorator from a wrapper and a target.

  Args:
    target: The final callable to be wrapped.
    decorator_func: The wrapper function.
    decorator_name: The name of the decorator. If `None`, the name of the
      function calling make_decorator.
    decorator_doc: Documentation specific to this application of
      `decorator_func` to `target`.
    decorator_argspec: Override the signature using FullArgSpec.

  Returns:
    The `decorator_func` argument with new metadata attached.
  """
if decorator_name is None:
    decorator_name = inspect.currentframe().f_back.f_code.co_name
decorator = TFDecorator(decorator_name, target, decorator_doc,
                        decorator_argspec)
setattr(decorator_func, '_tf_decorator', decorator)
# Objects that are callables (e.g., a functools.partial object) may not have
# the following attributes.
if hasattr(target, '__name__'):
    decorator_func.__name__ = target.__name__
if hasattr(target, '__qualname__'):
    decorator_func.__qualname__ = target.__qualname__
if hasattr(target, '__module__'):
    decorator_func.__module__ = target.__module__
if hasattr(target, '__dict__'):
    # Copy dict entries from target which are not overridden by decorator_func.
    for name in target.__dict__:
        if name not in decorator_func.__dict__:
            decorator_func.__dict__[name] = target.__dict__[name]
if hasattr(target, '__doc__'):
    decorator_func.__doc__ = decorator.__doc__
decorator_func.__wrapped__ = target
# Keeping a second handle to `target` allows callers to detect whether the
# decorator was modified using `rewrap`.
decorator_func.__original_wrapped__ = target
if decorator_argspec:
    decorator_func.__signature__ = fullargspec_to_signature(
        decorator_argspec)
elif callable(target):
    try:
        signature = inspect.signature(target)
    except (TypeError, ValueError):
        # Certain callables such as builtins can not be inspected for signature.
        pass
    else:
        bound_instance = _get_bound_instance(target)
        # Present the decorated func as a method as well
        if bound_instance and 'self' in signature.parameters:
            signature = inspect.Signature(list(signature.parameters.values())[1:])
            decorator_func.__self__ = bound_instance

        decorator_func.__signature__ = signature

exit(decorator_func)
