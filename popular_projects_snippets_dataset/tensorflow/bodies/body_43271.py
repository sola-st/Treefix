# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator.py
"""Injects a new target into a function built by make_decorator.

  This function allows replacing a function wrapped by `decorator_func`,
  assuming the decorator that wraps the function is written as described below.

  The decorator function must use `<decorator name>.__wrapped__` instead of the
  wrapped function that is normally used:

  Example:

      # Instead of this:
      def simple_parametrized_wrapper(*args, **kwds):
        return wrapped_fn(*args, **kwds)

      tf_decorator.make_decorator(simple_parametrized_wrapper, wrapped_fn)

      # Write this:
      def simple_parametrized_wrapper(*args, **kwds):
        return simple_parametrized_wrapper.__wrapped__(*args, **kwds)

      tf_decorator.make_decorator(simple_parametrized_wrapper, wrapped_fn)

  Note that this process modifies decorator_func.

  Args:
    decorator_func: Callable returned by `wrap`.
    previous_target: Callable that needs to be replaced.
    new_target: Callable to replace previous_target with.

  Returns:
    The updated decorator. If decorator_func is not a tf_decorator, new_target
    is returned.
  """
# Because the process mutates the decorator, we only need to alter the
# innermost function that wraps previous_target.
cur = decorator_func
innermost_decorator = None
target = None
while _has_tf_decorator_attr(cur):
    innermost_decorator = cur
    target = getattr(cur, '_tf_decorator')
    if target.decorated_target is previous_target:
        break
    cur = target.decorated_target
    assert cur is not None

# If decorator_func is not a decorator, new_target replaces it directly.
if innermost_decorator is None:
    # Consistency check. The caller should always pass the result of
    # tf_decorator.unwrap as previous_target. If decorator_func is not a
    # decorator, that will have returned decorator_func itself.
    assert decorator_func is previous_target
    exit(new_target)

target.decorated_target = new_target

if inspect.ismethod(innermost_decorator):
    # Bound methods can't be assigned attributes. Thankfully, they seem to
    # be just proxies for their unbound counterpart, and we can modify that.
    if hasattr(innermost_decorator, '__func__'):
        innermost_decorator.__func__.__wrapped__ = new_target
    elif hasattr(innermost_decorator, 'im_func'):
        innermost_decorator.im_func.__wrapped__ = new_target
    else:
        innermost_decorator.__wrapped__ = new_target
else:
    innermost_decorator.__wrapped__ = new_target

exit(decorator_func)
