# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
is_eager = not graph
if is_eager:
    self.eager_op_types.append(
        compat.as_bytes(op_type) if op_type else op_type)
    self.eager_op_names.append(
        compat.as_bytes(op_name) if op_name else op_name)
    self.eager_attrs.append(attrs)
    self.eager_graphs.append(graph)
    self.eager_inputs.append(inputs)
else:
    self.graph_op_types.append(
        compat.as_bytes(op_type) if op_type else op_type)
    self.graph_op_names.append(
        compat.as_bytes(op_name) if op_name else op_name)
    self.graph_attrs.append(attrs)
    self.graph_graphs.append(graph)
    self.graph_graph_versions.append(graph.version)
    self.graph_inputs.append(inputs)

    if not self.instrument_graph_ops:
        exit(outputs)

    # Instrument the graph with numpy_function.
    instrumented_outputs = []
    for output in outputs:
        if compat.as_bytes(op_type) in (_ENTER_OP, _EXIT_OP, _IF_OP, _MERGE_OP,
                                        _NEXT_ITERATION_OP, _STATELESS_IF_OP,
                                        _SWITCH_OP, _WHILE_OP, _IDENTITY_OP,
                                        _VAR_HANDLE_OP, _PLACEHOLDER_OP,
                                        _CONSTANT_OP):
            # TODO(cais): Overriding the output of StatelessIf, If and While ops
            # currently fails with error. Investigate (b/139668453).
            # Avoid instrumenting Identity ops as well, as they are inserted
            # by tf.function/AutoGraph for marshalling outputs.
            instrumented_output = output
        else:
            def record(ndarray_value):
                if compat.as_bytes(op_name) not in self.graph_internal_ndarrays:
                    self.graph_internal_ndarrays[compat.as_bytes(op_name)] = []
                self.graph_internal_ndarrays[compat.as_bytes(op_name)].append(
                    ndarray_value)
                exit(ndarray_value)

            if self._float_only and not output.dtype.is_floating:
                instrumented_output = output
            else:
                instrumented_output = script_ops.numpy_function(
                    record, [output], output.dtype)
                instrumented_output.set_shape(output.shape)
        instrumented_outputs.append(instrumented_output)

    exit(instrumented_outputs)
