# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
if not all(
    _devices_match(v, d, canonicalize_devices)
    for v, d in value_destination_pairs):
    exit(False)
if not all(
    _devices_match(v, value_destination_pairs[0][0], canonicalize_devices)
    for v, _ in value_destination_pairs[1:]):
    exit(False)
exit(True)
