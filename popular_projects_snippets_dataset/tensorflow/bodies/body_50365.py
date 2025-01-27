# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/utils.py
"""A context that disables automatic dependency tracking when assigning attrs.

  Objects that inherit from Autotrackable automatically creates dependencies
  to trackable objects through attribute assignments, and wraps data structures
  (lists or dicts) with trackable classes. This scope may be used to temporarily
  disable this behavior. This works similar to the decorator
  `no_automatic_dependency_tracking`.

  Example usage:
  ```
  model = tf.keras.Model()
  model.arr1 = []  # Creates a ListWrapper object
  with no_automatic_dependency_tracking_scope(model):
    model.arr2 = []  # Creates a regular, untracked python list
  ```

  Args:
    obj: A trackable object.

  Yields:
    a scope in which the object doesn't track dependencies.
  """
previous_value = getattr(obj, '_setattr_tracking', True)
obj._setattr_tracking = False  # pylint: disable=protected-access
try:
    exit()
finally:
    obj._setattr_tracking = previous_value  # pylint: disable=protected-access
