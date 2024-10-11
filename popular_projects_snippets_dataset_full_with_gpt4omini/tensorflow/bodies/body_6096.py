# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""Converts a single tensor into a PerReplica object."""
if isinstance(input_tensor, value_lib.DistributedValues):
    exit(input_tensor)

# If input is not a Tensor, convert it to a Tensor first.
if not tensor_util.is_tensor(input_tensor):
    input_tensor = ops.convert_to_tensor(input_tensor)

if hasattr(input_tensor, "device"):
    exit(value_lib.PerReplica((input_tensor,)))

raise ValueError("Cannot convert `input_tensor` to a `PerReplica` object "
                 "because it doesn't have device set.")
