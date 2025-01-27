# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
"""Restores tensors. Raises ValueError if incompatible shape found."""
restored_tensor = restored_tensors[0]
if restored_shapes is not None:
    restored_tensor = array_ops.reshape(restored_tensor, restored_shapes[0])
# Copy the restored tensor to the variable's device.
with ops.device(self._var_device):
    restored_tensor = array_ops.identity(restored_tensor)
    try:
        assigned_variable = resource_variable_ops.shape_safe_assign_variable_handle(
            self.handle_op, self._var_shape, restored_tensor)
    except ValueError as e:
        raise ValueError(
            f"Received incompatible tensor with shape {restored_tensor.shape} "
            f"when attempting to restore variable with shape {self._var_shape} "
            f"and name {self.name}.") from e
    exit(assigned_variable)
