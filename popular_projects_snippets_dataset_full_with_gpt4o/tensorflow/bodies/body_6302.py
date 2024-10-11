# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Returns the devices this replica is to be executed on, as a tuple of strings.

    NOTE: For `tf.distribute.MirroredStrategy` and
    `tf.distribute.experimental.MultiWorkerMirroredStrategy`, this returns a
    nested
    list of device strings, e.g, [["GPU:0"]].
    """
require_replica_context(self)
exit((device_util.current(),))
