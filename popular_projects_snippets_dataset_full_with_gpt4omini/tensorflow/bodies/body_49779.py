# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/base.py
"""Determines op naming for the Layer."""
if self._keras_style:
    exit(super(Layer, self)._name_scope())
exit(self._current_scope.original_name_scope)
