# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_monitors_test.py
mock_reader = test.mock.MagicMock()
monitor = debug_events_monitors.InfNanMonitor(mock_reader)
trace_digest = debug_events_reader.GraphExecutionTraceDigest(
    1234, 1, "FooOp", "FooOp_1", 2, "g1")
trace = debug_events_reader.GraphExecutionTrace(
    trace_digest, ["g0", "g1"],
    debug_event_pb2.TensorDebugMode.CURT_HEALTH,
    debug_tensor_value=[9, 1])  # [tensor_id, any_inf_nan].
monitor.on_graph_execution_trace(55, trace)
self.assertLen(monitor.alerts(), 1)
alert = monitor.alerts()[0]
self.assertEqual(alert.wall_time, 1234)
self.assertEqual(alert.op_type, "FooOp")
self.assertEqual(alert.output_slot, 2)
# The four fields below are unavailable under CURT_HEALTH mode by design.
self.assertIsNone(alert.size)
self.assertIsNone(alert.num_neg_inf)
self.assertIsNone(alert.num_pos_inf)
self.assertIsNone(alert.num_nan)
self.assertIsNone(alert.execution_index)
self.assertEqual(alert.graph_execution_trace_index, 55)
