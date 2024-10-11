# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer.py
"""Adds a `Graph` to the event file.

    The graph described by the protocol buffer will be displayed by
    TensorBoard. Most users pass a graph in the constructor instead.

    Args:
      graph: A `Graph` object, such as `sess.graph`.
      global_step: Number. Optional global step counter to record with the
        graph.
      graph_def: DEPRECATED. Use the `graph` parameter instead.

    Raises:
      ValueError: If both graph and graph_def are passed to the method.
    """

if graph is not None and graph_def is not None:
    raise ValueError("Please pass only graph, or graph_def (deprecated), "
                     "but not both.")

if isinstance(graph, ops.Graph) or isinstance(graph_def, ops.Graph):
    # The user passed a `Graph`.

    # Check if the user passed it via the graph or the graph_def argument and
    # correct for that.
    if not isinstance(graph, ops.Graph):
        logging.warning("When passing a `Graph` object, please use the `graph`"
                        " named argument instead of `graph_def`.")
        graph = graph_def

    # Serialize the graph with additional info.
    true_graph_def = graph.as_graph_def(add_shapes=True)
    self._write_plugin_assets(graph)
elif (isinstance(graph, graph_pb2.GraphDef) or
      isinstance(graph_def, graph_pb2.GraphDef)):
    # The user passed a `GraphDef`.
    logging.warning("Passing a `GraphDef` to the SummaryWriter is deprecated."
                    " Pass a `Graph` object instead, such as `sess.graph`.")

    # Check if the user passed it via the graph or the graph_def argument and
    # correct for that.
    if isinstance(graph, graph_pb2.GraphDef):
        true_graph_def = graph
    else:
        true_graph_def = graph_def

else:
    # The user passed neither `Graph`, nor `GraphDef`.
    raise TypeError("The passed graph must be an instance of `Graph` "
                    "or the deprecated `GraphDef`")
# Finally, add the graph_def to the summary writer.
self._add_graph_def(true_graph_def, global_step)
