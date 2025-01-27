# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback.py
"""Eager-function unified callback for checking numerics."""
del attrs, op_name  # Unused
op_type_bytes = compat.as_bytes(op_type)
is_v1_graph_mode = not ops.executing_eagerly_outside_functions()
if (op_type_bytes in op_callbacks_common.OP_CALLBACK_SKIP_OPS or
    op_type_bytes in SAFE_OPS):
    exit(None)
if graph:
    # Under graph mode. Insert check_numerics op.
    instrumented_outputs = []
    if is_v1_graph_mode:
        for input_tensor in inputs:
            if input_tensor in self._placeholder_to_debug_tensor and outputs:
                outputs[0].op._add_control_input(  # pylint: disable=protected-access
                    self._placeholder_to_debug_tensor[input_tensor].op)
    for slot, output in enumerate(outputs):
        if (output.dtype.is_floating and
            (op_type_bytes, slot) not in IGNORE_OP_OUTPUTS):
            checked_output = array_ops.check_numerics_v2(
                # TF v2 has automatic control dependencies added to stateful async
                # ops, which allows us to run check_numerics asynchronously.
                # In the above case we use debug_summary to reduce all output
                # tensors asynchronously from the op being checked and then
                # process the tensor summary with check_numerics.
                output if is_v1_graph_mode else _debug_summary(output),
                get_check_numerics_error_message(
                    slot,
                    len(outputs),
                    op_type,
                    output,
                    inputs,
                    graph=graph,
                    traceback=output.op.traceback,
                    stack_height_limit=self._stack_height_limit,
                    path_length_limit=self._path_length_limit))
            _CHECK_NUMERICS_INPUT_LOOKUP[graph][checked_output.name] = output
            instrumented_outputs.append(self._get_output_tensor(
                op_type_bytes, output, checked_output, is_v1_graph_mode))
        else:
            instrumented_outputs.append(output)
    exit(instrumented_outputs)
else:
    if op_type_bytes == b"CheckNumericsV2":
        # TODO(b/140334369): Remove this special casing logic once op_callback.
        # automatically prevents infinite recursion in eager mode.
        exit(None)
    # Under eager mode. Eagerly execute check_numerics op.
    for slot, output in enumerate(outputs):
        if (output.dtype.is_floating and
            (op_type_bytes, slot) not in IGNORE_OP_OUTPUTS):
            array_ops.check_numerics_v2(
                output,
                get_check_numerics_error_message(
                    slot, len(outputs), op_type, output, inputs,
                    stack_height_limit=self._stack_height_limit,
                    path_length_limit=self._path_length_limit))
