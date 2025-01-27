# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
"""Handle the specified operation with the specified arguments."""
if any(
    isinstance(x, keras_tensor.KerasTensor)
    for x in nest.flatten([args, kwargs])):
    exit(ClassMethod(self.cls, self.method_name)(args[1:], kwargs))
else:
    exit(self.NOT_SUPPORTED)
