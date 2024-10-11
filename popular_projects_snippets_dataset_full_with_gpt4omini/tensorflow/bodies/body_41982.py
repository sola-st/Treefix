# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/tracing_compiler.py
"""Gets a function for these inputs, defining it if necessary.

    Caller must hold self._lock.

    Args:
      args: The varargs for the Python function.
      kwargs: The keyword args for the Python function.

    Returns:
      A graph function corresponding to the input signature implied by args and
      kwargs, as well as filtered flattened inputs (only Tensors and Variables)
      that the object should be called with.

    Raises:
      ValueError: If inputs are incompatible with the input signature.
      TypeError: If the function inputs include non-hashable objects
      RuntimeError: If there's an internal bug (inconsistency) in handling
        shape relaxation retracing.
    """
args, kwargs, filtered_flat_args = (
    self._function_spec.canonicalize_function_inputs(args, kwargs))

if self.input_signature is not None:
    args = (*self.input_signature, *args[len(self.input_signature):])

# Get runtime values of captures
captures = self._func_captures.get_by_ref_snapshot()

current_func_context = function_context.make_function_context()

# cache_key_deletion_observer is useless here. It's based on all captures.
# A new cache key will be built later when saving ConcreteFunction because
# only active captures should be saved.
lookup_func_type, lookup_func_context = (
    self._function_spec.make_canonicalized_monomorphic_type(
        args, kwargs, captures))
concrete_function = self._function_cache.lookup(current_func_context,
                                                lookup_func_type)
if concrete_function is not None:
    exit((concrete_function, filtered_flat_args))

with monitoring.MonitoredTimer(_graph_building_time_counter.get_cell()):
    with trace.Trace("tf.function-graph_building"):
        logging.vlog(
            1, "Creating new FuncGraph for Python function %r (key: %r, %r)",
            self._python_function, current_func_context, lookup_func_type)
        logging.vlog(2, "Python function signature [args: %s] [kwargs: %s]",
                     args, kwargs)
        ag_status = (
            ag_ctx.Status.ENABLED
            if self._autograph else ag_ctx.Status.DISABLED)
        with ag_ctx.ControlStatusCtx(
            status=ag_status, options=self._autograph_options):
            func_graph = func_graph_module.FuncGraph(
                self._name, capture_by_value=self._capture_by_value)
            if self.input_signature is None and self._reduce_retracing:
                target_func_type = self._function_cache.generalize(
                    current_func_context, lookup_func_type)
            else:
                target_func_type = lookup_func_type
            handledata_mapping = lookup_func_context.get_handledata_mapping()
            placeholder_mapping = lookup_func_context.get_placeholder_mapping()
            placeholder_context = trace_type.InternalPlaceholderContext(
                func_graph, placeholder_mapping, handledata_mapping)
            with func_graph.as_default():
                placeholder_bound_args = target_func_type.placeholder_arguments(
                    placeholder_context)
            if self.function_spec.is_method:
                # TODO(fmuham): canonicalize_function_inputs removes self arg.
                args = placeholder_bound_args.args[1:]
            else:
                args = placeholder_bound_args.args
            kwargs = placeholder_bound_args.kwargs

            concrete_function = self._create_concrete_function(
                args, kwargs, func_graph)

            # TODO(b/263520817): Remove access to private attribute.
            graph_capture_container = concrete_function.graph._function_captures  # pylint: disable=protected-access
            # Maintain the list of all captures
            self._func_captures.merge_by_ref_with(graph_capture_container)
            # Get current active captures snapshot
            captures = graph_capture_container.get_by_ref_snapshot()

            # Create a cache_key with args and captures
            traced_func_deletion_observer = lookup_func_context.deletion_observer
            traced_func_type = _insert_capture_type(
                target_func_type, captures, lookup_func_context)

            self._function_cache.add(current_func_context, traced_func_type,
                                     traced_func_deletion_observer,
                                     concrete_function)

            exit((concrete_function, filtered_flat_args))
