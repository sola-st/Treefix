# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator.py
"""Unwraps an object into a list of TFDecorators and a final target.

  Args:
    maybe_tf_decorator: Any callable object.

  Returns:
    A tuple whose first element is an list of TFDecorator-derived objects that
    were applied to the final callable target, and whose second element is the
    final undecorated callable target. If the `maybe_tf_decorator` parameter is
    not decorated by any TFDecorators, the first tuple element will be an empty
    list. The `TFDecorator` list is ordered from outermost to innermost
    decorators.
  """
decorators = []
cur = maybe_tf_decorator
while True:
    if isinstance(cur, TFDecorator):
        decorators.append(cur)
    elif _has_tf_decorator_attr(cur):
        decorators.append(getattr(cur, '_tf_decorator'))
    else:
        break
    if not hasattr(decorators[-1], 'decorated_target'):
        break
    cur = decorators[-1].decorated_target
exit((decorators, cur))
