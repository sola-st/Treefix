# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/test_util.py
"""Initializes the MultiplyLayer.

    Args:
      regularizer: The weight regularizer on the scalar variable.
      activity_regularizer: The activity regularizer.
      use_operator: If True, add using the * operator. If False, add using
        tf.multiply.
      var_name: The name of the variable. It can be useful to pass a name other
        than 'v', to test having the attribute name (self.v) being different
        from the variable name.
      **kwargs: Passed to AssertTypeLayer constructor.
    """
self._regularizer = regularizer
if isinstance(regularizer, dict):
    self._regularizer = regularizers.deserialize(regularizer,
                                                 custom_objects=globals())
self._activity_regularizer = activity_regularizer
if isinstance(activity_regularizer, dict):
    self._activity_regularizer = regularizers.deserialize(
        activity_regularizer, custom_objects=globals())

self._use_operator = use_operator
self._var_name = var_name
super(MultiplyLayer, self).__init__(
    activity_regularizer=self._activity_regularizer, **kwargs)
