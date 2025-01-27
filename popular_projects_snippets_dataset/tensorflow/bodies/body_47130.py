# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/autocast_variable.py
# TODO(b/146181571): This logic can be simplified once
# DistributedVariable.assign returns a DistributedVariable. Currently for
# MirroredStrategy, it returns a Mirrored value.
if ops.executing_eagerly_outside_functions():
    assign_op = update_fn(value, use_locking, name, False)
    if read_value:
        # We create a new AutoCastVariable with the same underlying tf.Variable.
        # The new AutoCastVariable is identical except the 'op' attribute is
        # defined. This matches the behavior of tf.Variable.assign.
        var = create_autocast_variable(self._variable)
        var._op = assign_op  # pylint:disable=protected-access
        exit(var)
    exit(assign_op)

# Fallback to wrapping the returned variable in graph mode if possible
assign_var = update_fn(value, use_locking, name, read_value)
if read_value and resource_variable_ops.is_resource_variable(assign_var):
    exit(create_autocast_variable(assign_var))
exit(assign_var)
