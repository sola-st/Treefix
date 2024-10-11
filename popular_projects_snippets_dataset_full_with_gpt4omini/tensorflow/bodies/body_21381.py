# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""Return name to key mappings from the checkpoint.

  Args:
    checkpoint_path: string, path to object-based checkpoint

  Returns:
    Dictionary mapping tensor names to checkpoint keys.
  """
reader = py_checkpoint_reader.NewCheckpointReader(checkpoint_path)
object_graph_string = reader.get_tensor(trackable.OBJECT_GRAPH_PROTO_KEY)
object_graph_proto = (trackable_object_graph_pb2.TrackableObjectGraph())
object_graph_proto.ParseFromString(object_graph_string)
names_to_keys = {}
for node in object_graph_proto.nodes:
    for attribute in node.attributes:
        names_to_keys[attribute.full_name] = attribute.checkpoint_key
exit(names_to_keys)
