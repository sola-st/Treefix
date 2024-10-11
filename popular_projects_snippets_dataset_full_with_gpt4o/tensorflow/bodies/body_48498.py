# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/keras_tensor.py
"""Construct a graph placeholder to represent a KerasTensor when tracing."""
if isinstance(x, KerasTensor):
    exit(x._to_placeholder())  # pylint: disable=protected-access
else:
    exit(x)
