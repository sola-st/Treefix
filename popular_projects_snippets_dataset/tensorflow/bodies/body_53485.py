# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Creates a new, empty Graph."""
# Protects core state that can be returned via public accessors.
# Thread-safety is provided on a best-effort basis to support buggy
# programs, and is not guaranteed by the public `tf.Graph` API.
#
# NOTE(mrry): This does not protect the various stacks. A warning will
# be reported if these are used from multiple threads
self._lock = threading.RLock()
# The group lock synchronizes Session.run calls with methods that create
# and mutate ops (e.g. Graph.create_op()). This synchronization is
# necessary because it's illegal to modify an operation after it's been run.
# The group lock allows any number of threads to mutate ops at the same time
# but if any modification is going on, all Session.run calls have to wait.
# Similarly, if one or more Session.run calls are going on, all mutate ops
# have to wait until all Session.run calls have finished.
self._group_lock = lock_util.GroupLock(num_groups=2)
self._nodes_by_id = {}  # GUARDED_BY(self._lock)
self._next_id_counter = 0  # GUARDED_BY(self._lock)
self._nodes_by_name = {}  # GUARDED_BY(self._lock)
self._version = 0  # GUARDED_BY(self._lock)
# Maps a name used in the graph to the next id to use for that name.
self._names_in_use = {}
self._stack_state_is_thread_local = False
self._thread_local = threading.local()
# Functions that will be applied to choose a device if none is specified.
# In TF2.x or after switch_to_thread_local(),
# self._thread_local._device_function_stack is used instead.
self._graph_device_function_stack = traceable_stack.TraceableStack()
# Default original_op applied to new ops.
self._default_original_op = None
# Current control flow context. It could be either CondContext or
# WhileContext defined in ops/control_flow_ops.py
self._control_flow_context = None
# A new node will depend of the union of all of the nodes in the stack.
# In TF2.x or after switch_to_thread_local(),
# self._thread_local._control_dependencies_stack is used instead.
self._graph_control_dependencies_stack = []
# Arbitrary collections of objects.
self._collections = {}
# The graph-level random seed
self._seed = None
# A dictionary of attributes that should be applied to all ops.
self._attr_scope_map = {}
# A map from op type to the kernel label that should be used.
self._op_to_kernel_label_map = {}
# A map from op type to an alternative op type that should be used when
# computing gradients.
self._gradient_override_map = {}
# A map from op type to a gradient function that should be used instead.
self._gradient_function_map = {}
# True if the graph is considered "finalized".  In that case no
# new operations can be added.
self._finalized = False
# Functions defined in the graph
self._functions = collections.OrderedDict()
# Default GraphDef versions
self._graph_def_versions = versions_pb2.VersionDef(
    producer=versions.GRAPH_DEF_VERSION,
    min_consumer=versions.GRAPH_DEF_VERSION_MIN_CONSUMER)
self._building_function = False
# Stack of colocate_with ops. In TF2.x or after switch_to_thread_local(),
# self._thread_local._colocation_stack is used instead.
self._graph_colocation_stack = traceable_stack.TraceableStack()
# Set of tensors that are dangerous to feed!
self._unfeedable_tensors = object_identity.ObjectIdentitySet()
# Set of operations that are dangerous to fetch!
self._unfetchable_ops = set()
# A map of tensor handle placeholder to tensor dtype.
self._handle_feeders = {}
# A map from tensor handle to its read op.
self._handle_readers = {}
# A map from tensor handle to its move op.
self._handle_movers = {}
# A map from tensor handle to its delete op.
self._handle_deleters = {}
# Allow optimizers and other objects to pseudo-uniquely key graphs (this key
# will be shared when defining function graphs, for example, so optimizers
# being called inside function definitions behave as if they were seeing the
# actual outside graph).
self._graph_key = "graph-key-%d/" % (uid(),)
# A string with the last reduction method passed to
# losses.compute_weighted_loss(), or None. This is required only for
# backward compatibility with Estimator and optimizer V1 use cases.
self._last_loss_reduction = None
# Flag that is used to indicate whether loss has been scaled by optimizer.
# If this flag has been set, then estimator uses it to scale losss back
# before reporting. This is required only for backward compatibility with
# Estimator and optimizer V1 use cases.
self._is_loss_scaled_by_optimizer = False
self._container = ""

# The current AutomaticControlDependencies context manager.
self.experimental_acd_manager = None
# Set to True if this graph is being built in an
# AutomaticControlDependencies context.
# Deprecated: use acd_manager instead.
self._add_control_dependencies = False

# Cache for OpDef protobufs retrieved via the C API.
self._op_def_cache = {}
# Cache for constant results of `broadcast_gradient_args()`. The keys are
# tuples of fully-defined shapes: (x_shape_tuple, y_shape_tuple), and the
# values are tuples of reduction indices: (rx, ry).
self._bcast_grad_args_cache = {}
# Cache for constant results of `reduced_shape()`. The keys are pairs of
# tuples: (input_shape_tuple, reduction_indices_tuple), and the values
# are pairs of tuples: (output_shape_kept_dims, tile_scaling).
self._reduced_shape_cache = {}

# TODO(skyewm): fold as much of the above as possible into the C
# implementation
self._c_graph = c_api_util.ScopedTFGraph(self._graph_key)
# The C API requires all ops to have shape functions. Disable this
# requirement (many custom ops do not have shape functions, and we don't
# want to break these existing cases).
with self._c_graph.get() as c_graph:
    pywrap_tf_session.SetRequireShapeInferenceFns(c_graph, False)
if tf2.enabled():
    self.switch_to_thread_local()
