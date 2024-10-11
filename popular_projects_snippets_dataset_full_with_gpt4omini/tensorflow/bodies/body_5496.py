# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
"""Create a faked Mirrored object for testing.

  All components of the returned Mirrored have the same objects, which is not
  true in reality.
  """
devices = _get_devices(devices)
values = []
for d in devices:
    with ops.device(d):
        values.append(array_ops.identity(value))
exit(distribute_utils.regroup(
    values,
    wrap_class=value_lib.Mirrored))
