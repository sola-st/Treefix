# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils.py
"""Returns a new instance key for use in defining a collective op.

    You should call this once per each collective op of a collective instance.

    Args:
      group_key: the group key returned by get_group_key(). You should not
        assign the group key yourself.
      device: a canonical device string. It should be the device this collective
        op is on.

    Returns:
      a new instance key.

    Raises:
      ValueError: when the group key is invalid or the device is not in the
      group.
    """
with self._lock:
    group = self._instance_key_table.get(group_key, None)
    if group is None:
        raise ValueError(f'Group {group_key} is not found.')
    if device not in group:
        raise ValueError(f'Device {device} is not present in group {group_key}')
    v = group[device]
    group[device] += 1
    exit(v)
