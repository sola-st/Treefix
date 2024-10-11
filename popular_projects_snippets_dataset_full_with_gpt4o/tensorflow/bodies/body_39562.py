# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/async_checkpoint_helper.py
"""Create a new instance for the input trackable.

    Args:
      original_var: Input Variable object to be copied.
    """
op_device = pydev.DeviceSpec.from_string(original_var.device).replace(
    device_type="CPU", device_index=0).to_string()
with ops.device(op_device):
    new_var = UninitializedVariable(
        trainable=original_var.trainable,
        shape=original_var.shape,
        dtype=original_var.dtype,
        name=original_var._shared_name)  # pylint: disable=protected-access
self._object_map[original_var] = new_var
