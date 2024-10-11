# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
"""Constructs a new TensorFlow session.

    Args:
      target: (Optional) The TensorFlow execution engine to connect to.
      graph: (Optional) The graph to be used. If this argument is None, the
        default graph will be used.
      config: (Optional) ConfigProto proto used to configure the session. If no
        config is specified, the global default will be used. The global default
        can be configured via the tf.config APIs.

    Raises:
      tf.errors.OpError: Or one of its subclasses if an error occurs while
        creating the TensorFlow session.
      TypeError: If one of the arguments has the wrong type.
    """
_python_session_create_counter.get_cell().increase_by(1)
if graph is None:
    self._graph = ops.get_default_graph()
else:
    if not isinstance(graph, ops.Graph):
        raise TypeError('Argument `graph` must be a tf.Graph, but got '
                        f'"{type(graph).__name__}"')
    self._graph = graph

self._closed = False

if target is not None:
    try:
        self._target = compat.as_bytes(target)
    except TypeError:
        if isinstance(target, config_pb2.ConfigProto):
            raise TypeError('Argument `target` must be a string, but got '
                            f'"{type(target).__name__}". Did you do '
                            '"Session(config)" instead of '
                            '"Session(config=config)"?')
        raise TypeError('Argument `target` must be a string, but got '
                        f'"{type(target).__name__}"')
else:
    self._target = None

self._delete_lock = threading.Lock()
self._dead_handles = []

if config is None:
    config = context.context().config

if not isinstance(config, config_pb2.ConfigProto):
    raise TypeError('Argument `config` must be a tf.ConfigProto, but got '
                    f'"{type(config).__name__}"')

if (mixed_precision_global_state.is_mixed_precision_graph_rewrite_enabled()
    and config.graph_options.rewrite_options.auto_mixed_precision !=
    rewriter_config_pb2.RewriterConfig.OFF):
    new_config = config_pb2.ConfigProto()
    new_config.CopyFrom(config)
    new_config.graph_options.rewrite_options.auto_mixed_precision = (
        rewriter_config_pb2.RewriterConfig.ON)
    config = new_config
elif (config.graph_options.rewrite_options.auto_mixed_precision !=
      rewriter_config_pb2.RewriterConfig.ON):
    mixed_precision_global_state.set_non_mixed_precision_session_created(True)

self._config = config
self._add_shapes = config.graph_options.infer_shapes

self._session = None
opts = tf_session.TF_NewSessionOptions(target=self._target, config=config)
try:
    # pylint: disable=protected-access
    with self._graph._c_graph.get() as c_graph:
        self._session = tf_session.TF_NewSessionRef(c_graph, opts)
    # pylint: enable=protected-access
finally:
    tf_session.TF_DeleteSessionOptions(opts)
