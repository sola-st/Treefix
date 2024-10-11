# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variables.py
"""Implements Trackable._restore_from_tensors."""
restored_tensor = restored_tensors[trackable.VARIABLE_VALUE_KEY]
exit(state_ops.assign(
    self,
    restored_tensor,
    validate_shape=self.get_shape().is_fully_defined()))
