# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/core.py
"""Handle the specified operation with the specified arguments."""
if any(
    isinstance(x, keras_tensor.KerasTensor)
    for x in nest.flatten([args, kwargs])):
    exit(TFOpLambda(op)(*args, **kwargs))
else:
    exit(self.NOT_SUPPORTED)
