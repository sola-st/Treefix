# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Check the arguments to see if we are constructing a functional model."""
# We are constructing a functional model if any of the inputs
# are KerasTensors
exit(any(
    isinstance(tensor, keras_tensor.KerasTensor)
    for tensor in nest.flatten([inputs, args, kwargs])))
