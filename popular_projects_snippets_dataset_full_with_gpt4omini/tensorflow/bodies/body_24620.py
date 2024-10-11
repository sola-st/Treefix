# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_monitors_test.py
mock_reader = test.mock.MagicMock()
monitor = debug_events_monitors.InfNanMonitor(mock_reader)
trace_digest = debug_events_reader.GraphExecutionTraceDigest(
    1234, 1, "FooOp", "FooOp_1", 2, "g1")
trace = debug_events_reader.GraphExecutionTrace(
    trace_digest,
    ["g0", "g1"],
    debug_event_pb2.TensorDebugMode.CONCISE_HEALTH,
    # [tensor_id, size, num_neg_inf, num_pos_inf, num_nan].
    debug_tensor_value=[9, 100, 3, 2, 1])
monitor.on_graph_execution_trace(55, trace)

self.assertLen(monitor.alerts(), 1)
alert = monitor.alerts()[0]
self.assertEqual(alert.wall_time, 1234)
self.assertEqual(alert.op_type, "FooOp")
self.assertEqual(alert.output_slot, 2)
self.assertEqual(alert.size, 100)
self.assertEqual(alert.num_neg_inf, 3)
self.assertEqual(alert.num_pos_inf, 2)
self.assertEqual(alert.num_nan, 1)
self.assertEqual(alert.graph_execution_trace_index, 55)
