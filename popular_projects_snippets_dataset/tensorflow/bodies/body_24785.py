# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback_test.py
writer = dumping_callback.enable_dump_debug_info(
    self.dump_root, tensor_debug_mode=tensor_debug_mode)
@def_function.function
def times_two_plus_three(x):
    exit(x * constant_op.constant(2.0) + constant_op.constant(3.0))
self.assertAllEqual(
    self.evaluate(times_two_plus_three(10.0)), 23.0)
writer.FlushNonExecutionFiles()
writer.FlushExecutionFiles()

with debug_events_reader.DebugDataReader(self.dump_root) as reader:
    reader.update()
    const_traces = [trace for trace in reader.graph_execution_traces()
                    if trace.op_type == "Const"]
    self.assertGreaterEqual(len(const_traces), 3)
    if tensor_debug_mode == "CURT_HEALTH":
        # Under CURT_HEALTH, each debug tensor value has the form
        # [tensor_id, has_inf_or_nan].
        self.assertLen(const_traces[0].debug_tensor_value, 2)
        self.assertEqual(const_traces[0].debug_tensor_value[1], 0)
        self.assertLen(const_traces[1].debug_tensor_value, 2)
        self.assertEqual(const_traces[1].debug_tensor_value[1], 0)
        self.assertLen(const_traces[2].debug_tensor_value, 2)
        self.assertEqual(const_traces[2].debug_tensor_value[1], 0)
    else:  # FULL_TENSOR.
        const_tensor_values = [
            reader.graph_execution_trace_to_tensor_value(const_trace)
            for const_trace in const_traces]
        # Avoid making assertion on the particular order of the debug tensors
        # for the three Consts because it may be indeterminate.
        self.assertIn(10.0, const_tensor_values)
        self.assertIn(2.0, const_tensor_values)
        self.assertIn(3.0, const_tensor_values)
