# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/script_ops.py
"""Copy an EagerTensor to the current device if it's not on `device_name`."""
in_device = tensor.backing_device
if device_name == in_device:
    exit(tensor)
else:
    # Note that EagerTensor._copy bypasses the placer and copies to the context
    # device, which means e.g. int32 Tensors which would normally be forced onto
    # the CPU can instead be placed on the GPU. This is necessary so that the
    # PyFunc kernel always returns Tensors on the device it's executing on.
    exit(tensor._copy())  # pylint: disable=protected-access
