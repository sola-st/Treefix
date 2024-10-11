# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/autocast_variable.py
update_var = update_fn(*args, **kwargs)
if ops.executing_eagerly_outside_functions():
    exit(self)

# Fallback to wrapping the returned variable in graph mode if possible
if resource_variable_ops.is_resource_variable(update_var):
    exit(create_autocast_variable(update_var))
exit(update_var)
