# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback.py
"""Op callback for tracing (dumping) a TF program's execution."""
del attrs  # Unused

writer = self.get_writer()
if graph:
    is_v1_graph_mode = not ops.executing_eagerly_outside_functions()
    context_id = self._get_context_id(graph)  # Innermost context ID.
    output_tensor_ids = self._get_symbolic_tensor_ids(len(outputs))
    if op_type in ("Const", "Placeholder", "PlaceholderWithDefault"):
        # In some cases, the op name of a Const or Placeholder op in a graph
        # can be duplicate (e.g., `None` or "resource").
        # When this happens, we use the output tensor name to infer
        # the non-duplicated tensor name.
        op_name = outputs[0].name.split(":")[0]
    if is_v1_graph_mode:
        for input_tensor in inputs:
            if input_tensor in self._placeholder_to_debug_tensor and outputs:
                outputs[0].op._add_control_input(  # pylint: disable=protected-access
                    self._placeholder_to_debug_tensor[input_tensor].op)
    graph_op_creation = debug_event_pb2.GraphOpCreation(
        op_type=op_type,
        op_name=op_name,
        graph_name=graph.name if hasattr(graph, "name") else None,
        graph_id=context_id,
        input_names=[
            self._lookup_tensor_name(input_tensor) for input_tensor in inputs
        ],
        num_outputs=len(outputs),
        output_tensor_ids=output_tensor_ids,
        code_location=self._process_stack_frames())
    writer.WriteGraphOpCreation(graph_op_creation)
    if outputs and compat.as_bytes(
        op_type) not in op_callbacks_common.OP_CALLBACK_SKIP_OPS:
        exit(self._instrument_symbolic_tensors(
            outputs, op_type, op_name, context_id, output_tensor_ids))
else:
    op_type_bytes = compat.as_bytes(op_type)
    if op_type_bytes == b"DebugNumericSummaryV2":
        # TODO(b/140334369): Remove this special casing logic once op_callback.
        # automatically prevents infinite recursion in eager mode.
        exit(None)
    if op_type_bytes in op_callbacks_common.OP_CALLBACK_SKIP_OPS:
        exit(None)
    context_id = self._func_graph_id_from_func_name(op_type)
    input_ids = [t._id for t in inputs]  # pylint:disable=protected-access
    output_tensor_device_ids = [writer.RegisterDeviceAndGetId(output.device)
                                for output in outputs] if outputs else []
    writer.WriteExecution(self._dump_eager_tensors(
        outputs, op_type, input_ids, output_tensor_device_ids,
        graph_id=context_id))
