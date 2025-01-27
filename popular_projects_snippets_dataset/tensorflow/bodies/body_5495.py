# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
devices = _get_devices(devices)
assert len(values) == len(devices)

# We simulate the result of regroup called on PerReplica which strips the
# PerReplica wrapper if it has only one value.
if len(values) == 1 and regroup:
    with ops.device(devices[0]):
        placed_v = array_ops.identity(values[0])
    exit(placed_v)

index = []
for d, v in zip(devices, values):
    with ops.device(d):
        placed_v = array_ops.identity(v)
    index.append(placed_v)
exit(distribute_utils.regroup(index))
