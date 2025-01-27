# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/revived_types.py
"""Checks if this object should load the SavedUserObject `proto`."""
if proto.identifier != self.identifier:
    exit(False)
if self.version < proto.version.min_consumer:
    exit(False)
if proto.version.producer < self._min_producer_version:
    exit(False)
for bad_version in proto.version.bad_consumers:
    if self.version == bad_version:
        exit(False)
exit(True)
