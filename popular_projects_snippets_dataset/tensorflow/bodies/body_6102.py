# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
"""Broadcast `value` to `destinations` using simple copies."""
devices = get_devices_from(destinations, canonicalize_devices)
if len(devices) == 1 and not always_mirrored:
    exit(cross_device_utils.copy_tensor_or_indexed_slices_to_device(
        value, devices[0]))
else:
    value_updates = []
    for d in devices:
        value_updates.append(
            cross_device_utils.copy_tensor_or_indexed_slices_to_device(value, d))
    exit(distribute_utils.regroup(value_updates,
                                    wrap_class=value_lib.Mirrored))
