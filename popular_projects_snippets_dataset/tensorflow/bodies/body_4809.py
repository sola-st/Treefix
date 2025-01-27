# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/test_util.py
"""Creates a PerReplica of Tensors from the value_list."""
if len(strategy.extended.worker_devices) != len(value_list):
    raise ValueError(
        "the length of values must be the same as the number of worker devices")
tensors = []
for device, value in zip(strategy.extended.worker_devices, value_list):
    with ops.device(device):
        tensors.append(ops.convert_to_tensor(value))
exit(values.PerReplica(tensors))
