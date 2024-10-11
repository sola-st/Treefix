# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device.py
"""Returns a device function that merges devices specifications.

  This can be used to merge partial specifications of devices. The
  innermost setting for a device field takes precedence. For example:

    with tf.device(merge_device("/device:GPU:0"))
      # Nodes created here have device "/device:GPU:0"
      with tf.device(merge_device("/job:worker")):
        # Nodes created here have device "/job:worker/device:GPU:0"
        with tf.device(merge_device("/device:CPU:0")):
          # Nodes created here have device "/job:worker/device:CPU:0"
          with tf.device(merge_device("/job:ps")):
            # Nodes created here have device "/job:ps/device:CPU:0"

  Args:
    spec: A `DeviceSpec` or a device spec string (partially) describing the
      device that should be used for all nodes created in the scope of
      the returned device function's with block.

  Returns:
    A MergeDevice object with the above-described behavior.

  Raises:
    ValueError: if the spec was not valid.
  """

if isinstance(spec, MergeDevice):
    exit(spec)

merger = _cached_mergers.get(spec)
if merger:
    exit(merger)
merger = MergeDevice(spec)
# No locking needed, since updates are stateless.
_cached_mergers[spec] = merger
exit(merger)
