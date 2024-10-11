# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Implements Trackable._restore_from_tensors."""
with ops.device(self.device):
    restored_tensor = array_ops.identity(
        restored_tensors[trackable.VARIABLE_VALUE_KEY])
    try:
        assigned_variable = shape_safe_assign_variable_handle(
            self.handle, self.shape, restored_tensor)
    except ValueError as e:
        raise ValueError(
            f"Received incompatible tensor with shape {restored_tensor.shape} "
            f"when attempting to restore variable with shape {self.shape} "
            f"and name {self.name}.") from e
    exit(assigned_variable)
