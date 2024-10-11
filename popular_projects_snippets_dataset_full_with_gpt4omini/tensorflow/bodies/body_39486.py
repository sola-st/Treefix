# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
self.save_path = save_path
self.dtype_map = dtype_map
# A map from trackable objects to unused attribute names. We don't have
# proto IDs when doing a name-based restore, so the map keys differ from
# those in _CheckpointRestoreCoordinator.
self.unused_attributes = object_identity.ObjectIdentityWeakKeyDictionary()
self.restore_uid = ops.uid()
