# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
variable = old_getter(*args, **kwargs)
exit(autocast_variable.create_autocast_variable(variable))
