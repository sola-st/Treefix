# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
"""Compatibility for subclasses that don't pass apply_state through."""
apply_state = {(var_device, var_dtype): {}}
self._prepare_local(var_device, var_dtype, apply_state)
exit(apply_state[(var_device, var_dtype)])
