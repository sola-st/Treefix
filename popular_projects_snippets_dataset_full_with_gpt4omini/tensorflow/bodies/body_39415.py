# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_view.py
"""Configure the checkpoint view.

    Args:
      save_path: The path to the checkpoint.

    Raises:
      ValueError: If the save_path does not lead to a TF2 checkpoint.
    """

reader = py_checkpoint_reader.NewCheckpointReader(save_path)
try:
    object_graph_string = reader.get_tensor(base.OBJECT_GRAPH_PROTO_KEY)
except errors_impl.NotFoundError as not_found_error:
    raise ValueError(
        f"The specified checkpoint \"{save_path}\" does not appear to be "
        "object-based (saved with TF2) since it is missing the key "
        f"\"{base.OBJECT_GRAPH_PROTO_KEY}\". Likely it was created with the "
        "TF1 name-based saver and does not contain an object dependency graph."
    ) from not_found_error
object_graph_proto = (trackable_object_graph_pb2.TrackableObjectGraph())
object_graph_proto.ParseFromString(object_graph_string)
self._object_graph_proto = object_graph_proto
