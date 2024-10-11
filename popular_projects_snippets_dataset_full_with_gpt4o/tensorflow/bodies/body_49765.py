# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/variable_scope_shim.py
with vs.variable_creator_scope(
    self._variable_creator), vs.with_variable_store(self._var_store):
    exit()
