# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer.py
"""Creates a `SummaryWriter` and an event file.

    On construction the summary writer creates a new event file in `logdir`.
    This event file will contain `Event` protocol buffers constructed when you
    call one of the following functions: `add_summary()`, `add_session_log()`,
    `add_event()`, or `add_graph()`.

    If you pass a `Graph` to the constructor it is added to
    the event file. (This is equivalent to calling `add_graph()` later).

    TensorBoard will pick the graph from the file and display it graphically so
    you can interactively explore the graph you built. You will usually pass
    the graph from the session in which you launched it:

    ```python
    ...create a graph...
    # Launch the graph in a session.
    sess = tf.compat.v1.Session()
    # Create a summary writer, add the 'graph' to the event file.
    writer = tf.compat.v1.summary.FileWriter(<some-directory>, sess.graph)
    ```


    Args:
      event_writer: An EventWriter. Implements add_event and get_logdir.
      graph: A `Graph` object, such as `sess.graph`.
      graph_def: DEPRECATED: Use the `graph` argument instead.
    """
self.event_writer = event_writer
# For storing used tags for session.run() outputs.
self._session_run_tags = {}
if graph is not None or graph_def is not None:
    # Calling it with both graph and graph_def for backward compatibility.
    self.add_graph(graph=graph, graph_def=graph_def)
    # Also export the meta_graph_def in this case.
    # graph may itself be a graph_def due to positional arguments
    maybe_graph_as_def = (graph.as_graph_def(add_shapes=True)
                          if isinstance(graph, ops.Graph) else graph)
    self.add_meta_graph(
        meta_graph.create_meta_graph_def(graph_def=graph_def or
                                         maybe_graph_as_def))

# This set contains tags of Summary Values that have been encountered
# already. The motivation here is that the SummaryWriter only keeps the
# metadata property (which is a SummaryMetadata proto) of the first Summary
# Value encountered for each tag. The SummaryWriter strips away the
# SummaryMetadata for all subsequent Summary Values with tags seen
# previously. This saves space.
self._seen_summary_tags = set()
