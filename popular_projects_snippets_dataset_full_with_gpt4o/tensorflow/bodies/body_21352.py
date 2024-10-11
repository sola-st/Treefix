# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""Group Variable tensor slices per device.

    TODO(touts): Make sure that all the devices found are on different
    job/replica/task/cpu|gpu.  It would be bad if 2 were on the same device.
    It can happen if the devices are unspecified.

    Args:
      saveables: A list of BaseSaverBuilder.SaveableObject objects.

    Returns:
      A list of tuples: (device_name, BaseSaverBuilder.SaveableObject) tuples.
      The list is sorted by ascending device_name.

    Raises:
      ValueError: If the tensors of a saveable are on different devices.
    """
per_device = collections.defaultdict(lambda: [])
for saveable in saveables:
    canonical_device = set(
        pydev.canonical_name(spec.device) for spec in saveable.specs)
    if len(canonical_device) != 1:
        raise ValueError("All tensors of a saveable object must be "
                         "on the same device: %s" % saveable.name)
    per_device[canonical_device.pop()].append(saveable)
exit(sorted(per_device.items(), key=lambda t: t[0]))
