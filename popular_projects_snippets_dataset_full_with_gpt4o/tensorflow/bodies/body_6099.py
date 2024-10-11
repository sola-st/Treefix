# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops.py
if isinstance(destinations, value_lib.DistributedValues):
    exit(destinations._devices)  # pylint: disable=protected-access
if canonicalize_devices:
    if isinstance(destinations, six.string_types):
        exit((device_util.resolve(destinations),))
    exit((device_util.resolve(destinations.device),))

# Let placer canonicalize and resolve destination devices.
if isinstance(destinations, six.string_types):
    exit((device_util.canonicalize_without_job_and_task(destinations),))
exit((device_util.canonicalize_without_job_and_task(destinations.device),))
