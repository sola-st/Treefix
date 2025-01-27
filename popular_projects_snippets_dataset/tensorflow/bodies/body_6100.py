# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
exit(left is right or set(get_devices_from(
    left, canonicalize_devices)) == set(
        get_devices_from(right, canonicalize_devices)))
