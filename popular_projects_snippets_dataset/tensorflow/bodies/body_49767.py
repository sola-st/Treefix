# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/variable_scope_shim.py
super().__init__(**kwargs)
# Relies on keras layers tracking Modules
self.tracker = VariableAndLossTracker()
