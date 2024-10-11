# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/keras_tensor.py
"""Constructs a KerasTensor."""
if not isinstance(type_spec, type_spec_module.TypeSpec):
    raise ValueError('KerasTensors must be constructed with a `tf.TypeSpec`.')

self._type_spec = type_spec
self._inferred_value = inferred_value
self._name = name
