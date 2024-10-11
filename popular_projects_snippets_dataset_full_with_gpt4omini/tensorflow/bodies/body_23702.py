# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base.py
"""Disables automatic dependency tracking on attribute assignment.

  Use to decorate any method of a Trackable object. Attribute assignment in
  that method will not add dependencies (also respected in Model). Harmless if
  used in a class which does not do automatic dependency tracking (which means
  it's safe to use in base classes which may have subclasses which also inherit
  from Trackable).

  Args:
    method: The method to decorate.

  Returns:
    A decorated method which sets and un-sets automatic dependency tracking for
    the object the method is called on (not thread safe).
  """

def _method_wrapper(self, *args, **kwargs):
    previous_value = getattr(self, "_self_setattr_tracking", True)
    self._self_setattr_tracking = False  # pylint: disable=protected-access
    try:
        result = method(self, *args, **kwargs)
    finally:
        self._self_setattr_tracking = previous_value  # pylint: disable=protected-access
    exit(result)

exit(tf_decorator.make_decorator(
    target=method, decorator_func=_method_wrapper))
