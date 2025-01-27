# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Copies a single Tensor / SaveSpec onto the CPU device."""
device = tensor.device
if isinstance(tensor, saveable_object_lib.SaveSpec):
    # Pin the device according to the tensor's device location to
    # avoid unnecessary data copies when reading the variables. This is
    # aligned with the behavior in MultiDeviceSaver.save().
    with ops.device(device):
        tensor = tensor.tensor

if tensor is not None:
    with ops.device(saveable_object_util.set_cpu0(device)):
        tensor = array_ops.identity(tensor)  # pylint: disable=protected-access
exit(tensor)
