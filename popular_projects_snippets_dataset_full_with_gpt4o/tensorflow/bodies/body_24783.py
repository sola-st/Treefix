# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
writer = dumping_callback.enable_dump_debug_info(
    self.dump_root, tensor_debug_mode=tensor_debug_mode)

@def_function.function
def func(x, y):
    exit((x + y) / (x - y))

x = np.array([-3, -1, 0, 0, 1, 1, 1, 2], dtype=np.float16)
y = np.array([2, -1, 0, 0, 1, 1, 1, 3], dtype=np.float16)
# x - y = [-5, 0, 0, 0, 0, 0, 0, -1]
# (x + y) / (x - y) = [0.2, -inf, nan, nan, inf, inf, inf, -5].
self.evaluate(func(x, y))
writer.FlushNonExecutionFiles()
writer.FlushExecutionFiles()

with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    reader.update()
    graph_exec_traces = reader.graph_execution_traces()
    executed_op_types = [trace.op_type for trace in graph_exec_traces
                         if trace.op_type not in ["Const", "Placeholder"]]
    self.assertCountEqual(
        executed_op_types,
        ["AddV2", "Sub", "RealDiv"])
    if tensor_debug_mode == "CURT_HEALTH":
        for trace in graph_exec_traces:
            # 1st element: tensor_id, should be >= 0.
            # 2nd element: indicates if there is any inf or nan.
            tensor_id = reader.graph_execution_trace_to_tensor_id(trace)
            self.assertGreaterEqual(tensor_id, 0)
            if trace.op_type == "RealDiv":
                self.assertAllClose(trace.debug_tensor_value, [tensor_id, 1])
            else:
                self.assertAllClose(trace.debug_tensor_value, [tensor_id, 0])
    elif tensor_debug_mode == "CONCISE_HEALTH":
        for trace in graph_exec_traces:
            # 1st element: tensor_id, should be >= 0.
            # 2nd element: element count (8).
            # Remaining 3 elements: The counts of -inf, inf and nan.
            tensor_id = reader.graph_execution_trace_to_tensor_id(trace)
            self.assertGreaterEqual(tensor_id, 0)
            if trace.op_type == "RealDiv":
                self.assertAllClose(trace.debug_tensor_value,
                                    [tensor_id, 8, 1, 3, 2])
            else:
                self.assertAllClose(trace.debug_tensor_value,
                                    [tensor_id, 8, 0, 0, 0])
    elif tensor_debug_mode == "FULL_HEALTH":
        for trace in graph_exec_traces:
            # Elements: [
            #   -1 is the unset tensor_id for eager op execution,
            #   device ID (set to -1 for now),
            #   dtype, rank, element_count,
            #   neg_inf_count, pos_inf_count, nan_count
            #   neg_finite_count, zero_count, pos_finite_count]
            tensor_id = reader.graph_execution_trace_to_tensor_id(trace)
            self.assertGreaterEqual(tensor_id, 0)
            if trace.op_type == "RealDiv":
                self.assertAllClose(trace.debug_tensor_value,
                                    [tensor_id, -1, 19, 1, 8, 1, 3, 2, 1, 0, 1])
            elif trace.op_type == "Sub":
                self.assertAllClose(trace.debug_tensor_value,
                                    [tensor_id, -1, 19, 1, 8, 0, 0, 0, 2, 6, 0])
    else:  # SHAPE.
        for trace in graph_exec_traces:
            # 1st element: tensor_id, should be >= 0.
            # 2nd element: dtype enum value (float16 = 19).
            # 3rd element: rank (1)
            # 4th element: element count (8).
            # Remaining elements: shape at fixed length (6).
            tensor_id = reader.graph_execution_trace_to_tensor_id(trace)
            self.assertGreaterEqual(tensor_id, 0)
            self.assertAllClose(trace.debug_tensor_value,
                                [tensor_id, 19, 1, 8, 8, 0, 0, 0, 0, 0])
