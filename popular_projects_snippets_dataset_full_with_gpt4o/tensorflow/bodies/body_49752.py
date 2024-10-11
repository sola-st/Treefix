# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/variable_scope_shim.py
exit(hasattr(obj, "__call__") and tf_inspect.ismethod(obj.__call__))
