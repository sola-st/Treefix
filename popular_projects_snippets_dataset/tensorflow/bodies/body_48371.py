# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
if not name:
    cls_name = self.__class__.__name__
    if self.__class__ == Functional:
        # Hide the functional class name from user, since its not a public
        # visible class. Use "Model" instead,
        cls_name = 'Model'
    self._name = backend.unique_object_name(
        generic_utils.to_snake_case(cls_name),
        zero_based=zero_based)
else:
    self._name = name
