# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_monitors_test.py
mock_reader = test.mock.MagicMock()
mock_reader.graph_execution_trace_to_tensor_value.return_value = np.array(
    tensor_value, dtype=dtype)
monitor = debug_events_monitors.InfNanMonitor(mock_reader)
trace_digest = debug_events_reader.GraphExecutionTraceDigest(
    1234, 1, "BazOp", "name_scope_3/BazOp_1", 2, "g1")
trace = debug_events_reader.GraphExecutionTrace(
    trace_digest, ["g0", "g1"], debug_event_pb2.TensorDebugMode.FULL_TENSOR)
monitor.on_graph_execution_trace(80, trace)

if expected_num_neg_inf or expected_num_pos_inf or expected_num_nan:
    self.assertLen(monitor.alerts(), 1)
    alert = monitor.alerts()[0]
    self.assertEqual(alert.wall_time, 1234)
    self.assertEqual(alert.op_type, "BazOp")
    self.assertEqual(alert.output_slot, 2)
    self.assertEqual(alert.size, expected_size)
    self.assertEqual(alert.num_neg_inf, expected_num_neg_inf)
    self.assertEqual(alert.num_pos_inf, expected_num_pos_inf)
    self.assertEqual(alert.num_nan, expected_num_nan)
    self.assertIsNone(alert.execution_index)
    self.assertEqual(alert.graph_execution_trace_index, 80)
else:
    self.assertEmpty(monitor.alerts())
