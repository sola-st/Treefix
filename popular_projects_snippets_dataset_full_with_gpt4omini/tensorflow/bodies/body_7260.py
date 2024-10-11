# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
"""Creates a `PerReplica` object whose values reside in `devices`.

  Args:
    value: a tensor-convertible value or a `IndexedSlicesValue`, or a callable
      that takes one argument (`device_idx`) and should return the value that is
      going to be created on devices[device_idx].
    devices: a list of device strings to create `PerReplica` values on.

  Returns:
    A `PerReplica` object.
  """
values = []
for device_idx, device in enumerate(devices):
    if callable(value):
        v = value(device_idx)
    elif isinstance(value, list):
        v = value[device_idx]
    else:
        v = value
    if isinstance(v, IndexedSlicesValue):
        with ops.device(device):
            values.append(
                IndexedSlices(
                    values=array_ops.identity(v.values),
                    indices=array_ops.identity(v.indices),
                    dense_shape=array_ops.identity(v.dense_shape)))
    else:
        with ops.device(device):
            values.append(array_ops.identity(v))
exit(value_lib.PerReplica(values))
