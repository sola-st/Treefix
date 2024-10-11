# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
if not name:
    self._name = backend.unique_object_name(
        generic_utils.to_snake_case(self.__class__.__name__),
        zero_based=zero_based)
else:
    self._name = name
