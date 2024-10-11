# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Retrieves information about the objects in a checkpoint.

  Example usage:

  ```python
  object_graph = tf.contrib.checkpoint.object_metadata(
      tf.train.latest_checkpoint(checkpoint_directory))
  ckpt_variable_names = set()
  for node in object_graph.nodes:
    for attribute in node.attributes:
      ckpt_variable_names.add(attribute.full_name)
  ```

  Args:
    save_path: The path to the checkpoint, as returned by `save` or
      `tf.train.latest_checkpoint`.

  Returns:
    A parsed `tf.contrib.checkpoint.TrackableObjectGraph` protocol buffer.
  Raises:
    ValueError: If an object graph was not found in the checkpoint.
  """
reader = py_checkpoint_reader.NewCheckpointReader(save_path)
try:
    object_graph_string = reader.get_tensor(base.OBJECT_GRAPH_PROTO_KEY)
except errors_impl.NotFoundError:
    raise ValueError(
        f"The specified checkpoint \"{save_path}\" does not appear to be "
        "object-based (saved with TF2) since it is missing the key "
        f"\"{base.OBJECT_GRAPH_PROTO_KEY}\". Likely it was created with the "
        "TF1 name-based saver and does not contain an object dependency graph.")
object_graph_proto = (trackable_object_graph_pb2.TrackableObjectGraph())
object_graph_proto.ParseFromString(object_graph_string)
exit(object_graph_proto)
