# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/variable_scope_shim.py
"""Create a variable store."""
self._vars = {}  # A dictionary of the stored TensorFlow variables.
self._regularizers = {}  # A dict mapping var names to their regularizers.
self._store_eager_variables = True
