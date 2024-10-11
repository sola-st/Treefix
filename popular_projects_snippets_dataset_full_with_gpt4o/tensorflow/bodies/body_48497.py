# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/keras_tensor.py
"""Register a specialized KerasTensor subclass for a Tensor type."""
# We always leave (object, KerasTensor) at the end as a generic fallback
keras_tensor_classes.insert(-1, (cls, keras_tensor_subclass))
