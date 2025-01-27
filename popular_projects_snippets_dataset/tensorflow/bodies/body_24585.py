# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback.py
self._dump_root = dump_root
self._tfdbg_run_id = _get_tfdbg_run_id()
self._tensor_debug_mode = tensor_debug_mode
self._circular_buffer_size = circular_buffer_size
self._op_regex = op_regex
self._tensor_dtypes = tensor_dtypes

self._hostname = socket.gethostname()
# A list of source-file paths.
self._source_file_paths = []
# A map from stack frame (FileLineCol) to unique ID.
self._stack_frame_to_id = dict()
# Mapping op context to unique ID.
self._context_to_id = dict()
self._function_to_graph_id = dict()
self._op_type_to_context_id = dict()
# Keeps track of counter for symbolic tensors output by in-graph ops.
# It is used to make unique names for debugger-generated tensors.
self._symbolic_tensor_counter = 0
# A map from the names of debugger-generated Identity and DebugIdentityV2
# tensors to the names of the original insrumented graph tensors. This is
# applicable to v1 graph mode only.
self._tensor_aliases = dict()
self._source_file_paths_lock = threading.Lock()
self._stack_frame_to_id_lock = threading.Lock()
self._context_lock = threading.Lock()
self._symbolic_tensor_counter_lock = threading.Lock()
# A dict mapping Placeholder tensors to their instrumenting debug tensors.
# Used only under V1 graph mode, where we can't rely on auto control
# dependency to execute the debug tensors and hence need to attach the debug
# tensors as control dependencies of the ops that consume the Placeholder.
self._placeholder_to_debug_tensor = dict()
self._writer = None
