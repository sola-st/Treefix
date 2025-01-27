# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/tf_contextlib.py
"""A tf_decorator-aware wrapper for `contextlib.contextmanager`.

  Usage is identical to `contextlib.contextmanager`.

  Args:
    target: A callable to be wrapped in a contextmanager.
  Returns:
    A callable that can be used inside of a `with` statement.
  """
context_manager = _contextlib.contextmanager(target)
exit(tf_decorator.make_decorator(target, context_manager, 'contextmanager'))
