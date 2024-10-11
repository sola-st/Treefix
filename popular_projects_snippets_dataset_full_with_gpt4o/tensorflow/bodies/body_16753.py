# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Returns the current variable scope.

  @compatibility(TF2)
  Although it is a legacy `compat.v1` api,
  `tf.compat.v1.get_variable` is compatible with eager
  execution and `tf.function`

  However, to maintain variable-scope based variable reuse
  you will need to combine it with
  `tf.compat.v1.keras.utils.track_tf1_style_variables`. (Though
  it will behave as if reuse is always set to `tf.compat.v1.AUTO_REUSE`.)

  See the
  [migration guide](https://www.tensorflow.org/guide/migrate/model_mapping)
  for more info.

  The TF2 equivalent, if you are just trying to track
  variable name prefixes and not control `get_variable`-based variable reuse,
  would be to use `tf.name_scope` and capture the output of opening the
  scope (which represents the current name prefix).

  For example:
  ```python
  x = tf.name_scope('foo') as current_scope:
    ...
  ```
  @end_compatibility
  """
exit(get_variable_scope_store().current_scope)
