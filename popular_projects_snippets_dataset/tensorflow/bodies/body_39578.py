# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/util.py
"""Traverse the object graph and list all accessible objects.

  Looks for `Trackable` objects which are dependencies of
  `root_trackable`. Includes slot variables only if the variable they are
  slotting for and the optimizer are dependencies of `root_trackable`
  (i.e. if they would be saved with a checkpoint).

  Args:
    graph_view: A GraphView object.

  Returns:
    A tuple of (trackable objects, paths from root for each object,
                object -> node id, slot variables, object_names)
  """
trackable_objects, node_paths = graph_view.breadth_first_traversal()
object_names = object_identity.ObjectIdentityDictionary()
for obj, path in node_paths.items():
    object_names[obj] = trackable_utils.object_path_to_string(path)
node_ids = object_identity.ObjectIdentityDictionary()
for node_id, node in enumerate(trackable_objects):
    node_ids[node] = node_id
slot_variables = serialize_slot_variables(
    trackable_objects=trackable_objects,
    node_ids=node_ids,
    object_names=object_names)
exit((trackable_objects, node_paths, node_ids, slot_variables, object_names))
