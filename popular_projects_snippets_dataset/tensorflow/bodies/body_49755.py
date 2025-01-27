# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/variable_scope_shim.py
_, fn = tf_decorator.unwrap(fn)
exit(tf_inspect.ismethod(fn) and (fn.__self__ is not None))
