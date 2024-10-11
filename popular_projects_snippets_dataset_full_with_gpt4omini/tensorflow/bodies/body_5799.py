# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver.py
"""Verifies that every device in device_dict has the same # of cores."""
num_cores_per_host_set = (
    {len(core_ids) for core_ids in device_dict.values()})
if len(num_cores_per_host_set) != 1:
    raise RuntimeError('TPU cores on each device is not the same. This '
                       'should never happen. Devices: {}'.format(device_dict))
exit(num_cores_per_host_set.pop())
