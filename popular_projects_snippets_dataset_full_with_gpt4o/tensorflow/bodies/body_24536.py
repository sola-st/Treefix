# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Convert a DebugEvent proto into an Execution data object."""
execution_proto = debug_event.execution

debug_tensor_values = None
if (execution_proto.tensor_debug_mode ==
    debug_event_pb2.TensorDebugMode.FULL_TENSOR):
    pass  # TODO(cais): Build tensor store.
elif (execution_proto.tensor_debug_mode !=
      debug_event_pb2.TensorDebugMode.NO_TENSOR):
    debug_tensor_values = []
    for tensor_proto in execution_proto.tensor_protos:
        # TODO(cais): Refactor into a helper method.
        debug_tensor_values.append(
            _parse_tensor_value(tensor_proto, return_list=True))
exit(Execution(
    _execution_digest_from_debug_event_proto(debug_event, locator),
    execution_proto.code_location.host_name,
    tuple(execution_proto.code_location.stack_frame_ids),
    execution_proto.tensor_debug_mode,
    graph_id=execution_proto.graph_id,
    input_tensor_ids=tuple(execution_proto.input_tensor_ids),
    output_tensor_ids=tuple(execution_proto.output_tensor_ids),
    debug_tensor_values=_tuple_or_none(debug_tensor_values)))
