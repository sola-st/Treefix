# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Enables eager execution for the lifetime of this program.

  Most of the doc string for enable_eager_execution is relevant here as well.

  Args:
    config: See enable_eager_execution doc string
    device_policy: See enable_eager_execution doc string
    execution_mode: See enable_eager_execution doc string
    server_def: (Optional.) A tensorflow::ServerDef proto. Enables execution on
      remote devices. GrpcServers need to be started by creating an identical
      server_def to this, and setting the appropriate task_indexes, so that the
      servers can communicate. It will then be possible to execute operations on
      remote devices.

  Raises:
    ValueError

  """
if config is not None and not isinstance(config, config_pb2.ConfigProto):
    raise TypeError("config must be a tf.ConfigProto, but got %s" %
                    type(config))
if device_policy not in (None, context.DEVICE_PLACEMENT_EXPLICIT,
                         context.DEVICE_PLACEMENT_WARN,
                         context.DEVICE_PLACEMENT_SILENT,
                         context.DEVICE_PLACEMENT_SILENT_FOR_INT32):
    raise ValueError("device_policy must be one of None, DEVICE_PLACEMENT_*")
if execution_mode not in (None, context.SYNC, context.ASYNC):
    raise ValueError("execution_mode must be one of None, SYNC, " "ASYNC")
if context.default_execution_mode == context.GRAPH_MODE:
    graph_mode_has_been_used = (
        _default_graph_stack._global_default_graph is not None)  # pylint: disable=protected-access
    if graph_mode_has_been_used:
        raise ValueError(
            "tf.enable_eager_execution must be called at program startup.")
context.default_execution_mode = context.EAGER_MODE
# pylint: disable=protected-access
with context._context_lock:
    if context._context is None:
        context._set_context_locked(context.Context(
            config=config,
            device_policy=device_policy,
            execution_mode=execution_mode,
            server_def=server_def))
    elif ((config is not None and config is not context._context._config) or
          (device_policy is not None and
           device_policy is not context._context._device_policy) or
          (execution_mode is not None and
           execution_mode is not context._context._execution_mode)):
        raise ValueError(
            "Trying to change the options of an active eager"
            " execution. Context config: %s, specified config:"
            " %s. Context device policy: %s, specified device"
            " policy: %s. Context execution mode: %s, "
            " specified execution mode %s." %
            (context._context._config, config, context._context._device_policy,
             device_policy, context._context._execution_mode, execution_mode))
    else:
        # We already created everything, so update the thread local data.
        context._context._thread_local_data.is_eager = True

  # Monkey patch to get rid of an unnecessary conditional since the context is
  # now initialized.
context.context = context.context_safe
