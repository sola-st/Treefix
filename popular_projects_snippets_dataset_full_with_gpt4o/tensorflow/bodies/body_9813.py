# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""Creates a new TensorFlow session.

    If no `graph` argument is specified when constructing the session,
    the default graph will be launched in the session. If you are
    using more than one graph (created with `tf.Graph()`) in the same
    process, you will have to use different sessions for each graph,
    but each graph can be used in multiple sessions. In this case, it
    is often clearer to pass the graph to be launched explicitly to
    the session constructor.

    Args:
      target: (Optional.) The execution engine to connect to. Defaults to using
        an in-process engine. See
        [Distributed TensorFlow](https://tensorflow.org/deploy/distributed) for
          more examples.
      graph: (Optional.) The `Graph` to be launched (described above).
      config: (Optional.) A
        [`ConfigProto`](https://www.tensorflow.org/code/tensorflow/core/protobuf/config.proto)
          protocol buffer with configuration options for the session.
    """
super(Session, self).__init__(target, graph, config=config)
# NOTE(mrry): Create these on first `__enter__` to avoid a reference cycle.
self._default_graph_context_manager = None
self._default_session_context_manager = None
