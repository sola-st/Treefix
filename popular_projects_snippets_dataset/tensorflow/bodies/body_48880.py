# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
variable = old_getter(*args, **kwargs)
exit(autocast_variable.create_autocast_variable(variable))
