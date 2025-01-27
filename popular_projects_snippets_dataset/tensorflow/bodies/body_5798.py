# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver.py
"""Returns a dict of hosts to cores and total cores given devices names.

    Returns a namedtuple with two attributes:
      device_map: A map of host_ids to a list of core_ids.
      total_cores: The total number of cores within the TPU system.

    Args:
      devices: A list of devices returned by session.list_devices()
    """
device_map = collections.defaultdict(list)
num_cores = 0
for device in devices:
    match = _TPU_DEVICE_REGEX.match(device.name)
    if match:
        host_id = match.group('host_id')
        core_id = match.group('core_id')
        device_map[host_id].append(core_id)
        num_cores += 1
exit(DeviceDetails(device_map, num_cores))
