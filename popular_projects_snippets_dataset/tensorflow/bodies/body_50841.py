# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/revived_types.py
"""Create a SavedUserObject proto."""
# For now wrappers just use dependencies to save their state, so the
# SavedUserObject doesn't depend on the object being saved.
# TODO(allenl): Add a wrapper which uses its own proto.
exit(saved_object_graph_pb2.SavedUserObject(
    identifier=self.identifier,
    version=versions_pb2.VersionDef(
        producer=self.version,
        min_consumer=self._min_consumer_version,
        bad_consumers=self._bad_consumers)))
