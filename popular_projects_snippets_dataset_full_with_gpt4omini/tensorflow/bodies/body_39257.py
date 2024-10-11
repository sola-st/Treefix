# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/restore.py
"""Specify an object within a checkpoint.

    Args:
      checkpoint: A _CheckpointRestoreCoordinator object.
      proto_id: The index of this object in TrackableObjectGraph.nodes.
    """
self._checkpoint = checkpoint
self._proto_id = proto_id
# This may be set to True if the registered saver cannot be used with this
# object.
self.skip_restore = False
