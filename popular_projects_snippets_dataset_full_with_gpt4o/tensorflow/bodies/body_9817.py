# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""Creates a new interactive TensorFlow session.

    If no `graph` argument is specified when constructing the session,
    the default graph will be launched in the session. If you are
    using more than one graph (created with `tf.Graph()`) in the same
    process, you will have to use different sessions for each graph,
    but each graph can be used in multiple sessions. In this case, it
    is often clearer to pass the graph to be launched explicitly to
    the session constructor.

    Args:
      target: (Optional.) The execution engine to connect to. Defaults to using
        an in-process engine.
      graph: (Optional.) The `Graph` to be launched (described above).
      config: (Optional) `ConfigProto` proto used to configure the session.
    """
if not config:
    # If config is not provided, choose some reasonable defaults for
    # interactive use:
    #
    #   - Grow GPU memory as needed at the cost of fragmentation.
    gpu_options = config_pb2.GPUOptions(allow_growth=True)
    config = config_pb2.ConfigProto(gpu_options=gpu_options)
# Interactive sessions always place pruned graphs.
config.graph_options.place_pruned_graph = True

super(InteractiveSession, self).__init__(target, graph, config)
with InteractiveSession._count_lock:
    if InteractiveSession._active_session_count > 0:
        warnings.warn('An interactive session is already active. This can '
                      'cause out-of-memory errors in some cases. You must '
                      'explicitly call `InteractiveSession.close()` to release '
                      'resources held by the other session(s).')
    InteractiveSession._active_session_count += 1
# NOTE(mrry): We do not use `Session._closed` here because it has unhelpful
# semantics (in particular, it is not set to true if `Session.close()` is
# called on a session that has not been "opened" by running a step) and we
# cannot change those semantics without breaking existing code.
self._explicitly_closed = False

self._default_session = self.as_default()
self._default_session.enforce_nesting = False
self._default_session.__enter__()
self._explicit_graph = graph
if self._explicit_graph is not None:
    self._default_graph = graph.as_default()
    self._default_graph.enforce_nesting = False
    self._default_graph.__enter__()
