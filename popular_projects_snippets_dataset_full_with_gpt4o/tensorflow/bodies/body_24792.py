# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
x = constant_op.constant(2.0)
y = constant_op.constant(3.0)
writer = dumping_callback.enable_dump_debug_info(
    self.dump_root, tensor_debug_mode=tensor_debug_mode)

@def_function.function
def log_sum(x, y):
    exit(math_ops.log(x + y))

@def_function.function
def sin1p_log_sum(x, y):
    exit(math_ops.sin(1.0 + log_sum(x, y)))

self.assertAllClose(sin1p_log_sum(x, y), np.sin(1.0 + np.log(5.0)))
writer.FlushNonExecutionFiles()
writer.FlushExecutionFiles()

with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    reader.update()
    outermost_graphs = reader.outermost_graphs()
    self.assertLen(outermost_graphs, 1)

    if context.executing_eagerly():
        # NOTE(b/142486213): Execution of the TF function happens with
        # Session.run() in v1 graph mode, so doesn't get logged to the
        # .execution file.
        executions = reader.executions()
        self.assertLen(executions, 1)
        self.assertIn("sin1p_log_sum", executions[0].op_type)
        # Get the executed graph and verify its identity and inner graph.
        graph = reader.graph_by_id(executions[0].graph_id)
        self.assertEqual(graph.name, "sin1p_log_sum")
        self.assertLen(graph.inner_graph_ids, 1)
        inner_graph = reader.graph_by_id(graph.inner_graph_ids[0])
        self.assertEqual(inner_graph.name, "log_sum")
        # Check device names.
        self.assertLen(executions[0].output_tensor_device_ids, 1)
        self.assertEqual(
            reader.device_name_by_id(executions[0].output_tensor_device_ids[0]),
            self._expectedDefaultDeviceName())
        self.assertIn(self._expectedDefaultDeviceName(),
                      set(reader.device_name_map().values()))

    # Verify the recorded graph-building history.
    add_op_digests = reader.graph_op_digests(op_type="AddV2")
    self.assertLen(add_op_digests, 2)
    self.assertEqual(
        reader.graph_by_id(add_op_digests[0].graph_id).name, "log_sum")
    self.assertEqual(
        reader.graph_by_id(add_op_digests[1].graph_id).name, "sin1p_log_sum")
    log_op_digests = reader.graph_op_digests(op_type="Log")
    self.assertLen(log_op_digests, 1)
    self.assertEqual(
        reader.graph_by_id(log_op_digests[0].graph_id).name, "log_sum")
    sin_op_digests = reader.graph_op_digests(op_type="Sin")
    self.assertLen(sin_op_digests, 1)
    self.assertEqual(
        reader.graph_by_id(sin_op_digests[0].graph_id).name, "sin1p_log_sum")

    # Verify the output tensor IDs and the stack traces.
    for op_digest in add_op_digests + log_op_digests + sin_op_digests:
        # These are all single-output ops.
        self.assertLen(op_digest.output_tensor_ids, 1)
        self.assertGreaterEqual(op_digest.output_tensor_ids[0], 0)
        _, stack_frames = reader.read_graph_op_creation_stack_trace(op_digest)
        self._verifyStackFrames(stack_frames)

    graph_exec_traces = [trace for trace in reader.graph_execution_traces()
                         if trace.op_type not in ["Const", "Placeholder"]]
    executed_op_types = [digest.op_type for digest in graph_exec_traces]
    self.assertEqual(
        executed_op_types, ["AddV2", "Log", "AddV2", "Sin"])

    # Verify the graph ID stack of each op.
    # 1st AddV2 op.
    self.assertEqual(
        reader.graph_by_id(graph_exec_traces[0].graph_ids[-1]).name,
        "log_sum")
    self.assertEqual(
        reader.graph_by_id(graph_exec_traces[0].graph_ids[-2]).name,
        "sin1p_log_sum")
    # Log op.
    self.assertEqual(
        reader.graph_by_id(graph_exec_traces[1].graph_ids[-1]).name,
        "log_sum")
    self.assertEqual(
        reader.graph_by_id(graph_exec_traces[1].graph_ids[-2]).name,
        "sin1p_log_sum")
    # 2nd AddV2 op.
    self.assertEqual(
        reader.graph_by_id(graph_exec_traces[2].graph_ids[-1]).name,
        "sin1p_log_sum")
    # Sin op.
    self.assertEqual(
        reader.graph_by_id(graph_exec_traces[3].graph_ids[-1]).name,
        "sin1p_log_sum")

    if tensor_debug_mode == "NO_TENSOR":
        # Under the default NO_TENSOR tensor-debug mode, the tensor_proto ought
        # to be an empty float32 tensor.
        for trace in graph_exec_traces:
            self.assertIsNone(trace.debug_tensor_value)
    elif tensor_debug_mode == "CURT_HEALTH":
        # Test the association between graph exec and prior graph building.
        # In each case, the 1st element of debug_tensor_value is the ID of the
        # symbolic tenosr and the 2nd element is a zero indicating there is no
        # inf or nan.
        self.assertAllClose(  # 1st AddV2 op.
            graph_exec_traces[0].debug_tensor_value,
            [add_op_digests[0].output_tensor_ids[0], 0.0])
        self.assertAllClose(  # Log op.
            graph_exec_traces[1].debug_tensor_value,
            [log_op_digests[0].output_tensor_ids[0], 0.0])
        self.assertAllClose(  # 2nd AddV2 op.
            graph_exec_traces[2].debug_tensor_value,
            [add_op_digests[1].output_tensor_ids[0], 0.0])
        self.assertAllClose(  # Sin op.
            graph_exec_traces[3].debug_tensor_value,
            [sin_op_digests[0].output_tensor_ids[0], 0.0])
    elif tensor_debug_mode == "CONCISE_HEALTH":
        # 1st element: tensor_id.
        # 2nd element: element count. Remaining elements: all zero because there
        # is no -inf, inf or nan.
        # 1st AddV2 op.
        self.assertAllClose(
            graph_exec_traces[0].debug_tensor_value,
            [add_op_digests[0].output_tensor_ids[0], 1.0, 0.0, 0.0, 0.0])
        # Log op.
        self.assertAllClose(
            graph_exec_traces[1].debug_tensor_value,
            [log_op_digests[0].output_tensor_ids[0], 1.0, 0.0, 0.0, 0.0])
        # 2nd AddV2 op.
        self.assertAllClose(
            graph_exec_traces[2].debug_tensor_value,
            [add_op_digests[1].output_tensor_ids[0], 1.0, 0.0, 0.0, 0.0])
        # Sin op.
        self.assertAllClose(
            graph_exec_traces[3].debug_tensor_value,
            [sin_op_digests[0].output_tensor_ids[0], 1.0, 0.0, 0.0, 0.0])
    elif tensor_debug_mode == "FULL_HEALTH":
        # Elements: [
        #   -1 is the unset tensor_id for eager op execution,
        #   device ID (set to -1 for now),
        #   dtype, rank, element_count,
        #   neg_inf_count, pos_inf_count, nan_count
        #   neg_finite_count, zero_count, pos_finite_count]
        # 1st AddV2 op.
        self.assertAllClose(
            graph_exec_traces[0].debug_tensor_value,
            [add_op_digests[0].output_tensor_ids[0],
             -1, 1, 0, 1, 0, 0, 0, 0, 0, 1])
        # Log op.
        self.assertAllClose(
            graph_exec_traces[1].debug_tensor_value,
            [log_op_digests[0].output_tensor_ids[0],
             -1, 1, 0, 1, 0, 0, 0, 0, 0, 1])
        # 2nd AddV2 op.
        self.assertAllClose(
            graph_exec_traces[2].debug_tensor_value,
            [add_op_digests[1].output_tensor_ids[0],
             -1, 1, 0, 1, 0, 0, 0, 0, 0, 1])
        # Sin op.
        self.assertAllClose(
            graph_exec_traces[3].debug_tensor_value,
            [sin_op_digests[0].output_tensor_ids[0],
             -1, 1, 0, 1, 0, 0, 0, 0, 0, 1])
    elif tensor_debug_mode == "SHAPE":
        # 1st element: tensor_id.
        # 2nd element: dtype (float32).
        # 3rd element: rank (scalar).
        # 4th element: element count (1).
        # Remaining elements: shape padded to fixed length (6).
        # 1st AddV2 op.
        self.assertAllClose(
            graph_exec_traces[0].debug_tensor_value,
            [add_op_digests[0].output_tensor_ids[0], 1, 0, 1, 0, 0, 0, 0, 0, 0])
        # Log op.
        self.assertAllClose(
            graph_exec_traces[1].debug_tensor_value,
            [log_op_digests[0].output_tensor_ids[0], 1, 0, 1, 0, 0, 0, 0, 0, 0])
        # 2nd AddV2 op.
        self.assertAllClose(
            graph_exec_traces[2].debug_tensor_value,
            [add_op_digests[1].output_tensor_ids[0], 1, 0, 1, 0, 0, 0, 0, 0, 0])
        # Sin op.
        self.assertAllClose(
            graph_exec_traces[3].debug_tensor_value,
            [sin_op_digests[0].output_tensor_ids[0], 1, 0, 1, 0, 0, 0, 0, 0, 0])
    else:  # FULL_TENSOR.

        full_tensor_values = [
            reader.graph_execution_trace_to_tensor_value(trace)
            for trace in graph_exec_traces]
        self.assertAllClose(
            full_tensor_values[0], 5.0)  # 1st AddV2 op.
        self.assertAllClose(
            full_tensor_values[1], np.log(5.0))  # Log op.
        self.assertAllClose(
            full_tensor_values[2],
            np.log(5.0) + 1.0)  # 2nd AddV2 op.
        self.assertAllClose(
            full_tensor_values[3],
            np.sin(np.log(5.0) + 1.0))  # Sin op.
