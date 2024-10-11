# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_server.py
"""Callback for Event proto received through the gRPC stream.

    This Event proto carries a GraphDef, encoded as bytes, in its graph_def
    field.

    Args:
      graph_def: A GraphDef object.
      device_name: Name of the device on which the graph was created.
      wall_time: An epoch timestamp (in microseconds) for the graph.

    Returns:
      `None` or an `EventReply` proto to be sent back to the client. If `None`,
      an `EventReply` proto construct with the default no-arg constructor will
      be sent back to the client.
    """
raise NotImplementedError(
    "on_graph_def() is not implemented in the base servicer class")
