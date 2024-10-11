# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/base.py
"""A context that disables manual dependency tracking for the given `obj`.

  Sometimes library methods might track objects on their own and we might want
  to disable that and do the tracking on our own. One can then use this context
  manager to disable the tracking the library method does and do your own
  tracking.

  For example:

  class TestLayer(tf.keras.Layer):
    def build():
      with no_manual_dependency_tracking_scope(self):
        var = self.add_variable("name1")  # Creates a var and doesn't track it
      self._track_trackable("name2", var)  # We track variable with name `name2`

  Args:
    obj: A trackable object.

  Yields:
    a scope in which the object doesn't track dependencies manually.
  """
# pylint: disable=protected-access
previous_value = getattr(obj, "_manual_tracking", True)
obj._manual_tracking = False
try:
    exit()
finally:
    obj._manual_tracking = previous_value
