# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Enables eager execution for the lifetime of this program.

  Eager execution provides an imperative interface to TensorFlow. With eager
  execution enabled, TensorFlow functions execute operations immediately (as
  opposed to adding to a graph to be executed later in a `tf.compat.v1.Session`)
  and
  return concrete values (as opposed to symbolic references to a node in a
  computational graph).

  For example:

  ```python
  tf.compat.v1.enable_eager_execution()

  # After eager execution is enabled, operations are executed as they are
  # defined and Tensor objects hold concrete values, which can be accessed as
  # numpy.ndarray`s through the numpy() method.
  assert tf.multiply(6, 7).numpy() == 42
  ```

  Eager execution cannot be enabled after TensorFlow APIs have been used to
  create or execute graphs. It is typically recommended to invoke this function
  at program startup and not in a library (as most libraries should be usable
  both with and without eager execution).

  @compatibility(TF2)
  This function is not necessary if you are using TF2. Eager execution is
  enabled by default.
  @end_compatibility

  Args:
    config: (Optional.) A `tf.compat.v1.ConfigProto` to use to configure the
      environment in which operations are executed. Note that
      `tf.compat.v1.ConfigProto` is also used to configure graph execution (via
      `tf.compat.v1.Session`) and many options within `tf.compat.v1.ConfigProto`
      are not implemented (or are irrelevant) when eager execution is enabled.
    device_policy: (Optional.) Policy controlling how operations requiring
      inputs on a specific device (e.g., a GPU 0) handle inputs on a different
      device  (e.g. GPU 1 or CPU). When set to None, an appropriate value will
      be picked automatically. The value picked may change between TensorFlow
      releases.
      Valid values:
      - DEVICE_PLACEMENT_EXPLICIT: raises an error if the
        placement is not correct.
      - DEVICE_PLACEMENT_WARN: copies the tensors which are not
        on the right device but logs a warning.
      - DEVICE_PLACEMENT_SILENT: silently copies the tensors.
        Note that this may hide performance problems as there is no notification
        provided when operations are blocked on the tensor being copied between
        devices.
      - DEVICE_PLACEMENT_SILENT_FOR_INT32: silently copies
        int32 tensors, raising errors on the other ones.
    execution_mode: (Optional.) Policy controlling how operations dispatched are
      actually executed. When set to None, an appropriate value will be picked
      automatically. The value picked may change between TensorFlow releases.
      Valid values:
      - SYNC: executes each operation synchronously.
      - ASYNC: executes each operation asynchronously. These
        operations may return "non-ready" handles.

  Raises:
    ValueError: If eager execution is enabled after creating/executing a
     TensorFlow graph, or if options provided conflict with a previous call
     to this function.
  """
_api_usage_gauge.get_cell().set(True)
logging.vlog(1, "Enabling eager execution")
if context.default_execution_mode != context.EAGER_MODE:
    exit(enable_eager_execution_internal(
        config=config,
        device_policy=device_policy,
        execution_mode=execution_mode,
        server_def=None))
