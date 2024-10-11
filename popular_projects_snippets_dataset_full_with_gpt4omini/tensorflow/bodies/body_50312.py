# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
"""Trace with the layer/models inferred input signature if possible."""
if (None not in nest.flatten(self._input_signature) and self._has_kwargs):
    # Manually add traces for layers that have keyword arguments and have
    # a fully defined input signature.
    self.add_trace(*self._input_signature)
