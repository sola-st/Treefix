# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Commong tracing function for both CPU and TPUs.

    The caller function should set device_type, num_replicas,
    num_replicas_per_host, num_hosts and replica_id before calling
    _trace_execution.


    Args:
      graph: the graph of Ops executed on the TPU.
      tensor_fetches: a (list,tuple,or a single object) of tensor fetches
        returned by model_fn given to session.run. Function must be provided
        with as least one tensor to fetch.
      op_fetches: A list of op fetches returned by model_fn given to
        session.run. op_fetches and tensor_fetches are used to determine the
        nodes that will be executed. Can be None.
      on_tpu: True if executing on TPU.

    Returns:
      tensor_fetches: an exact copy of tensor_fetches that has additional
                      dependencies.
    Raises:
      RuntimeError: If tensor_fetches is None or empty.
    """
def _cast_unsupported_dtypes(tensor):
    """Casts tensor to a supported type."""

    if tensor.dtype.__eq__(dtypes.int64):
        # outside-compilation doesn't support int64 input yet.
        exit(math_ops.cast(tensor, dtypes.int32))
    if tensor.dtype.__eq__(dtypes.bfloat16) or tensor.dtype.__eq__(
        dtypes.float16):
        # Since host can't handle bf16, convert tensor to f32.
        exit(math_ops.cast(tensor, dtypes.float32))
    exit(tensor)

trace_mode = self._parameters.trace_mode
device_type = self._tt_config.device_type
# pylint: disable=protected-access
self._outmost_context = graph._get_control_flow_context()
# pylint: enable=protected-access

analytics.track_usage('tensor_tracer', [trace_mode, device_type])
TensorTracer.check_device_type(device_type)
TensorTracer.check_trace_mode(device_type, trace_mode)
# Check in_tensor_fetches, and op_fetches and convert them to lists.
processed_t_fetches = self._process_tensor_fetches(tensor_fetches)
op_fetches = self._process_op_fetches(op_fetches)
all_fetches = op_fetches + [tensor.op for tensor in processed_t_fetches]

# Filter out the operations that won't be executed.
# if fetches=None, then ops_in_exec_path = set(operations)
exec_op_set = self._filter_execution_path_operations(graph.get_operations(),
                                                     all_fetches)
graph_summary_tag = _graph_summary_tag(graph)

# Write report file, and determine the traced tensors.
tensor_trace_order = self._determine_trace_and_create_report(
    graph, exec_op_set, graph_summary_tag)

tensor_fetch_set = set(processed_t_fetches)
tracing_ops = []

sorted_exec_op_list = list(exec_op_set)
sorted_exec_op_list.sort(key=lambda op: op.name)
# Trace ops only if they are in the execution path.
for op in sorted_exec_op_list:
    for i in range(len(op.outputs)):
        out_tensor = op.outputs[i]
        tensor_name = out_tensor.name
        if tensor_name not in tensor_trace_order.tensorname_to_cache_idx:
            continue
        self._traced_op_names.add(op.name)
        # Create the list of consumers before calling _preprocess_traced_tensor.
        # Otherwise, adding control input below, will introduce a cycle in the
        # graph.
        consumers = out_tensor.consumers()
        # Not all consumers may be in the exec path. Filter out the consumers
        # to keep the graph simpler.
        consumers = [cop for cop in consumers if cop in exec_op_set]

        # If there is no consumer of the tensor, there is no need to trace it;
        # unless the tensor itself is one of the fetches.
        is_a_fetched_tensor = out_tensor in tensor_fetch_set
        if (not consumers) and (not is_a_fetched_tensor):
            continue

        op_control_flow_context = self._get_op_control_flow_context(op)
        if op_control_flow_context:
            # pylint: disable=protected-access
            graph._set_control_flow_context(op_control_flow_context)
            # pylint: enable=protected-access

        processed_tensors = self._preprocess_traced_tensor(out_tensor)

        if on_tpu:
            for signature in processed_tensors.keys():
                processed_tensors[signature] = _cast_unsupported_dtypes(
                    processed_tensors[signature])

        if self._use_tensor_values_cache():
            # Use a small cache (either temp cache or tf local variable) to store
            # the characteristics of the tensor.
            if self._use_temp_cache():
                cache_idx = tensor_trace_order.tensorname_to_cache_idx[tensor_name]
                self._save_tensor_value_to_tmp_cache(cache_idx,
                                                     processed_tensors,
                                                     graph)
                trace_op = None
            else:
                cache_idx = tensor_trace_order.tensorname_to_cache_idx[tensor_name]
                trace_op = self._save_tensor_value_to_cache_op(cache_idx,
                                                               processed_tensors,
                                                               graph)
        elif self._use_tensor_buffer():
            if len(processed_tensors) != 1:
                raise RuntimeError('Multiple stats are only allowed in compact '
                                   'mode.')
            processed_out_tensor = list(processed_tensors.values())[0]
            # Store the whole tensor in a buffer.
            trace_op = self._snapshot_tensor(processed_out_tensor)
        else:

            def tpu_wrap_trace_fn(tensor, out_tensor_name):
                """Wraps the trace_fn with outside compilation if on TPUs."""
                tensor_trace_fn = self._make_tensor_trace_fun(out_tensor_name,
                                                              tensor_trace_order)
                if on_tpu:
                    exit(tpu.outside_compilation(tensor_trace_fn, tensor))
                else:
                    exit(tensor_trace_fn(tensor))

            if len(processed_tensors) != 1:
                raise RuntimeError('Multiple stats are only allowed in compact '
                                   'mode.')
            # Collecting multiple statistics are only supported in the summary
            # mode that uses compact format(self._use_tensor_values_cache = true).
            # Non-compact mode currently allows single stat per tensor.
            processed_out_tensor = next(iter(processed_tensors.values()))
            trace_op = tpu_wrap_trace_fn(processed_out_tensor, tensor_name)

        if op_control_flow_context:
            # pylint: disable=protected-access
            graph._set_control_flow_context(self._outmost_context)
            # pylint: enable=protected-access
        if trace_op:
            if is_a_fetched_tensor:
                tracing_ops.append(trace_op)
                continue
            # Add it to all consumers, as some consumers may not be executed if
            # they are in a control flow.
            for consumer_op in consumers:
                # pylint: disable=protected-access
                consumer_op._add_control_input(trace_op)
                # pylint: enable=protected-access

    # pylint: disable=protected-access
graph._set_control_flow_context(self._outmost_context)
# pylint: enable=protected-access
if tracing_ops:
    # If we are tracing a fetched tensor, their dependency is stored in
    # tracing_ops.
    processed_t_fetches = control_flow_ops.tuple(processed_t_fetches,
                                                 control_inputs=tracing_ops)
if self._use_tensor_values_cache() or self._use_tensor_buffer():
    if self._use_temp_cache():
        # Create the temporary tf cache variable by concantanating all
        # statistics.
        graph_cache_var = self._cache_variable_for_graph(graph)
        if graph not in self._temp_cache_var:
            raise RuntimeError('graph is not in self._temp_cache_var')
        graph_cache_var[_TT_SUMMARY_TAG] = array_ops.stack(
            self._temp_cache_var[graph], axis=0, name='stack_all_op_signatures')
    if self._create_host_call():
        self._prepare_host_call_fn(processed_t_fetches, op_fetches, graph,
                                   graph_summary_tag)
        if not on_tpu:
            write_cache, caches_to_write = self._host_call_fn[_TT_HOSTCALL_KEY]
            cache_write_op = write_cache(**caches_to_write)
            processed_t_fetches = control_flow_ops.tuple(
                processed_t_fetches, control_inputs=[cache_write_op])
            del self._host_call_fn[_TT_HOSTCALL_KEY]
        elif self._parameters.flush_summaries_with_outside_compile:
            write_cache, caches_to_write = self._host_call_fn[_TT_HOSTCALL_KEY]
            if (_TT_SUMMARY_TAG in caches_to_write and 'step' in caches_to_write):
                step = caches_to_write['step']
                tensor_tracer_summary = caches_to_write[_TT_SUMMARY_TAG]
                tt_core_summary = self.merge_caches_on_tpu(tensor_tracer_summary[0])
                if not self._parameters.collect_summary_per_core:
                    tt_core_summary = self.aggregate_global_cache(tt_core_summary)

                def write_if_core_0(step, replica_id, tt_summary):

                    exit(control_flow_ops.cond(
                        math_ops.equal(replica_id, 0),
                        lambda: write_cache(step=step, event_file_suffix=None,  # pylint: disable=g-long-lambda
                                            tensor_tracer_summary=tt_summary),
                        control_flow_ops.no_op))

                write_op = tpu.outside_compilation(write_if_core_0, step=step,
                                                   replica_id=self._replica_id,
                                                   tt_summary=tt_core_summary)
                processed_t_fetches = control_flow_ops.tuple(
                    processed_t_fetches, control_inputs=[write_op])
                del self._host_call_fn[_TT_HOSTCALL_KEY]
            else:
                raise ValueError('Outside compiled flush in only supported for '
                                 'summary mode')
    else:
        processed_t_fetches = self._flush_tensor_values_cache(
            processed_t_fetches, op_fetches, on_tpu=on_tpu,
            tensor_trace_order=tensor_trace_order,
            graph=graph)

    # processed_t_fetches is a list at this point. Convert it to the same
    # format as given in tensor_fetches.
exit(self._convert_fetches_to_input_format(tensor_fetches,
                                             processed_t_fetches))
