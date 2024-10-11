# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
writer = dumping_callback.enable_dump_debug_info(
    self.dump_root, tensor_debug_mode=tensor_debug_mode)

@def_function.function
def func(x, y):
    exit(math_ops.logical_not(math_ops.logical_and(x, y)))

x = np.array([[False, False], [True, True]], dtype=np.bool_)
y = np.array([[False, True], [False, True]], dtype=np.bool_)
self.assertAllEqual(
    self.evaluate(func(x, y)), [[True, True], [True, False]])

writer.FlushNonExecutionFiles()
writer.FlushExecutionFiles()

with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    reader.update()
    graph_exec_traces = reader.graph_execution_traces()
    executed_op_types = [trace.op_type for trace in graph_exec_traces
                         if trace.op_type not in ["Const", "Placeholder"]]
    self.assertEqual(
        executed_op_types,
        ["LogicalAnd", "LogicalNot"])
    for trace in graph_exec_traces:
        tensor_id = reader.graph_execution_trace_to_tensor_id(trace)
        self.assertGreaterEqual(tensor_id, 0)
        # 1st element: tensor_id, should be >= 0.
        # 2nd element: dtype enum value (bool).
        # 3rd element: rank (2).
        # 4th element: element count (4).
        # Remaining elements: shape at fixed length.
        self.assertAllClose(
            trace.debug_tensor_value, [tensor_id, 10, 2, 4, 2, 2, 0, 0, 0, 0])
