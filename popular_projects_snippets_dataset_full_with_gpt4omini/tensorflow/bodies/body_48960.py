# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
if not name:
    self._name = backend.unique_object_name(
        generic_utils.to_snake_case(self.__class__.__name__),
        zero_based=zero_based)
else:
    backend.observe_object_name(name)
    self._name = name
