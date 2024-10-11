# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Walk the object graph, using global names for SaveableObjects."""
objects = util.list_objects(self._object_graph_view)
saveable_objects = []
for trackable in objects:
    # pylint: disable=protected-access
    trackable._maybe_initialize_trackable()
    if trackable._update_uid < self._checkpoint.restore_uid:
        trackable._update_uid = self._checkpoint.restore_uid
    else:
        continue
    # pylint: enable=protected-access
    saveable_objects.extend(
        self._checkpoint.globally_named_object_attributes(trackable))
exit(saveable_objects)
