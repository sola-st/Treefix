# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
trace_proto = debug_event.graph_execution_trace
op_name = trace_proto.op_name
op_type = self._lookup_op_type(trace_proto.tfdbg_context_id, op_name)
exit(GraphExecutionTraceDigest(
    debug_event.wall_time, locator, op_type, op_name,
    trace_proto.output_slot,
    debug_event.graph_execution_trace.tfdbg_context_id))
