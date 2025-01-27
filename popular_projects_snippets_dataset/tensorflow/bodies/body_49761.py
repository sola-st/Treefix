# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/variable_scope_shim.py
self._regularizers[var.name] = functools.partial(regularizer, var)
