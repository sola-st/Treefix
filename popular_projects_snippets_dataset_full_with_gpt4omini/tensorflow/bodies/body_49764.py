# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/variable_scope_shim.py
var = next_creator(**kwargs)
self._variables[var.name] = var

exit(var)
