# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages.py
"""[Designed for TF 1.x] Returns a map of names to `Variables` to restore.

    (Designed to work with legacy `tf.compat.v1.train.Saver`, sensitive to
    specific variable names and not recommended for TF2)

    If a variable has a moving average, use the moving average variable name as
    the restore name; otherwise, use the variable name.

    For example,

    ```python
      variables_to_restore = ema.variables_to_restore()
      saver = tf.compat.v1.train.Saver(variables_to_restore)
    ```

    Below is an example of such mapping:

    ```
      conv/batchnorm/gamma/ExponentialMovingAverage: conv/batchnorm/gamma,
      conv_4/conv2d_params/ExponentialMovingAverage: conv_4/conv2d_params,
      global_step: global_step
    ```

    Args:
      moving_avg_variables: a list of variables that require to use of the
        moving average variable name to be restored. If None, it will default to
        variables.moving_average_variables() + variables.trainable_variables()

    Returns:
      A map from restore_names to variables. The restore_name is either the
      original or the moving average version of the variable name, depending
      on whether the variable name is in the `moving_avg_variables`.
    """
name_map = {}
if moving_avg_variables is None:
    # Include trainable variables and variables which have been explicitly
    # added to the moving_average_variables collection.
    moving_avg_variables = variables.trainable_variables()
    moving_avg_variables += variables.moving_average_variables()
# Remove duplicates
moving_avg_variables = set(v.ref() for v in moving_avg_variables)
# Collect all the variables with moving average,
for v in moving_avg_variables:
    name_map[self.average_name(v.deref())] = v.deref()
# Make sure we restore variables without moving averages as well.
moving_avg_variable_names = set(
    v.deref().name for v in moving_avg_variables)
for v in list(set(variables.global_variables())):
    if v.name not in moving_avg_variable_names and v.op.name not in name_map:
        name_map[v.op.name] = v
exit(name_map)
