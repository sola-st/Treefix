# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Construct a new FuncGraph.

    The graph will inherit its graph key, collections, seed, and distribution
    strategy stack from the current context or graph.

    Args:
      name: the name of the function.
      collections: a dictionary of collections this FuncGraph should start with.
        If not specified (None), the FuncGraph will read (but not write to) the
        outer graph's collections that are not allowlisted, and both read and
        write to the outer graph's collections that are allowlisted. The current
        allowlisted collections are the global variables, the local variables,
        and the trainable variables. Defaults to None.
      capture_by_value: An optional boolean. If True, the func graph will
        capture Variables by value instead of reference. By default inherit from
        outer graphs, and failing that will default to False.
      structured_input_signature: Optional. The structured input signature to
        use for initializing the FuncGraph. See the docstring for FuncGraph for
        more information.
      structured_outputs: Optional. The structured outputs to use for
        initializing the FuncGraph. See the docstring for FuncGraph for more
        information.
    """
super().__init__()
self.name = name
self.inputs = []
self.outputs = []
self.control_outputs = []
self.control_captures = object_identity.ObjectIdentitySet()
self.structured_input_signature = structured_input_signature
self.structured_outputs = structured_outputs
self._resource_tensor_inputs = object_identity.ObjectIdentitySet()
self._weak_variables = []
self._watched_variables = object_identity.ObjectIdentityWeakSet()
self.is_control_flow_graph = False

self._function_captures = capture_container.FunctionCaptures()
outer_graph = ops.get_default_graph()
self._weak_outer_graph = weakref.ref(outer_graph)
while outer_graph.building_function:
    outer_graph = outer_graph.outer_graph
# If self._weak_outer_graph is deleted, we revert to the outermost Graph
# active when the FuncGraph was traced. This will not be a FuncGraph.
self._fallback_outer_graph = outer_graph
self._captures = py_collections.OrderedDict()
# If not None, records the names of output args of this function. Used to
# preserve the output names in the signature of a serialized+deserialized
# function. Private at the moment mostly because it's often out of date.
self._output_names = None
# Maps arbitrary key -> (closure, nest of placeholders), where at function
# call time the value of closure() will be used to feed the nest of
# placeholders.
self._deferred_captures = py_collections.OrderedDict()
# Inherit capture-by-value from outer graph.
if capture_by_value is not None:
    self.capture_by_value = capture_by_value
elif self.outer_graph is not None and isinstance(self.outer_graph,
                                                 FuncGraph):
    self.capture_by_value = self.outer_graph.capture_by_value
else:
    self.capture_by_value = False

self._building_function = True

graph = self.outer_graph

if context.executing_eagerly():
    self.seed = context.global_seed()
    # [for tf-data user migration from TF1.0 to 2.0] seed_used keep track of
    # any None op_seed for random_op in the function, in which case we end up
    # using function seed, which could be unintended behavior for the op.
    self._seed_used = False
else:
    self.seed = graph.seed
    self._seed_used = False
    # TODO(allenl): Figure out if we can remove colocation stack
    # specialization (currently used in cond_v2), here and in the cache key.
    self._colocation_stack = graph._colocation_stack.copy()  # pylint: disable=protected-access

if collections is None:
    for collection_name in graph.get_all_collection_keys():
        if collection_name not in ALLOWLIST_COLLECTIONS:
            self._collections[collection_name] = graph.get_collection(
                collection_name)
    for collection_name in ALLOWLIST_COLLECTIONS:
        self._collections[collection_name] = graph.get_collection_ref(
            collection_name)
else:
    self._collections = collections

# Keep track of whether this FuncGraph is exportable to SavedModel. Use
# `graph.mark_as_unsaveable(reason)` to mark this FuncGraph and any
# dependent functions as unsaveable.
self._saveable = True
self._saving_errors = set()

# Keep track of callbacks to run when this graph exits default scope
self._scope_exit_callbacks = None
