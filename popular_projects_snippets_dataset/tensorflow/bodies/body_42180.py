# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Creates a new Context.

    Args:
      config: (Optional.) A `ConfigProto` protocol buffer with configuration
        options for the Context. Note that a lot of these options may be
        currently unimplemented or irrelevant when eager execution is enabled.
      device_policy: (Optional.) What policy to use when trying to run an
        operation on a device with inputs which are not on that device. When set
        to None, an appropriate value will be picked automatically. The value
        picked may change between TensorFlow releases.  Defaults to
        DEVICE_PLACEMENT_SILENT.
        Valid values:
        - DEVICE_PLACEMENT_EXPLICIT: raises an error if the placement is not
          correct.
        - DEVICE_PLACEMENT_WARN: copies the tensors which are not on the right
          device but raises a warning.
        - DEVICE_PLACEMENT_SILENT: silently copies the tensors. This might hide
          performance problems.
        - DEVICE_PLACEMENT_SILENT_FOR_INT32: silently copies int32 tensors,
          raising errors on the other ones.
      execution_mode: (Optional.) Policy controlling how operations dispatched
        are actually executed. When set to None, an appropriate value will be
        picked automatically. The value picked may change between TensorFlow
        releases.
        Valid values:
        - SYNC: executes each operation synchronously.
        - ASYNC: executes each operation asynchronously. These operations may
          return "non-ready" handles.
      server_def: (Optional.) A tensorflow::ServerDef proto. Enables execution
        on remote devices. GrpcServers need to be started by creating an
        identical server_def to this, and setting the appropriate task_indexes,
        so that the servers can communicate. It will then be possible to execute
        operations on remote devices.

    Raises:
     ValueError: If execution_mode is not valid.
    """
# This _id is used only to index the tensor caches.
# TODO(iga): Remove this when tensor caches are moved to C++.
self._id = _context_id_counter.increment_and_get()
self._tensor_cache_deleter = _TensorCacheDeleter(self._id)
_tensor_caches_map[self._id] = _TensorCaches()

self._config = config
self._thread_local_data = pywrap_tfe.EagerContextThreadLocalData(
    self,
    is_eager=lambda: default_execution_mode == EAGER_MODE,
    device_spec=_starting_device_spec)
self._context_switches = _ContextSwitchStack(self.executing_eagerly())
self._context_handle = None
self._context_devices = None
self._seed = None
self._initialize_lock = threading.Lock()
self._initialized = False
if device_policy is None:
    device_policy = DEVICE_PLACEMENT_SILENT
self._device_policy = device_policy
self._mirroring_policy = None
if execution_mode not in (None, SYNC, ASYNC):
    raise ValueError("execution_mode should be None/SYNC/ASYNC. Got %s" %
                     execution_mode)
if execution_mode is None:
    execution_mode = SYNC
self._default_is_async = execution_mode == ASYNC
self._use_tfrt = is_tfrt_enabled()
self._jit_compile_rewrite = jit_compile_rewrite_enabled()
self._server_def = server_def
self._collective_ops_server_def = None
self._collective_leader = None
self._collective_scoped_allocator_enabled_ops = None
self._collective_use_nccl_communication = None
self._collective_device_filters = None
self._coordination_service_config = None

self._device_lock = threading.Lock()
self._physical_devices = None
self._physical_device_to_index = None
self._pluggable_devices = None
self._visible_device_list = []
self._memory_growth_map = None
self._virtual_device_map = {}

# Values set after construction
self._optimizer_jit = None
self._intra_op_parallelism_threads = None
self._inter_op_parallelism_threads = None
self._soft_device_placement = None
self._log_device_placement = None
self._operation_timeout_in_ms = None
self._enable_mlir_graph_optimization = None
self._optimizer_experimental_options = {}

_python_eager_context_create_counter.get_cell().increase_by(1)

self._is_global_context = False
