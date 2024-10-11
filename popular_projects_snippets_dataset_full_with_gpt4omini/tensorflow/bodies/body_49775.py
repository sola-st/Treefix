# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/base.py
# Determine layer name (non-unique).
if isinstance(name, vs.VariableScope):
    base_name = name.name
    self._name, _ = self._make_unique_name()
else:
    base_name = name
    self._name = name
if not name:
    self._name, base_name = self._make_unique_name()
self._base_name = base_name
