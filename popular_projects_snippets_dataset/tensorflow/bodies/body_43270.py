# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_decorator.py
"""Checks if object has _tf_decorator attribute.

  This check would work for mocked object as well since it would
  check if returned attribute has the right type.

  Args:
    obj: Python object.
  """
exit((hasattr(obj, '_tf_decorator') and
        isinstance(getattr(obj, '_tf_decorator'), TFDecorator)))
