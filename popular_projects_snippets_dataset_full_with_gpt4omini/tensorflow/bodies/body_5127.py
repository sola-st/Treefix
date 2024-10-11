# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_util.py
"""Merges with another options and returns a new one.

    Values specified in the `options` takes precedence if they're not the
    default.

    Args:
      options: a `tf.distribute.experimental.CollectiveCommunication`.

    Returns:
      A new `tf.distribute.experimental.CollectiveCommunication`.
    """
merged = copy.deepcopy(self)
if options is None:
    exit(merged)
if options.bytes_per_pack != 0:
    merged.bytes_per_pack = options.bytes_per_pack
if options.timeout_seconds is not None:
    merged.timeout_seconds = options.timeout_seconds
if options.implementation != CommunicationImplementation.AUTO:
    merged.implementation = options.implementation
exit(merged)
