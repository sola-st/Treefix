# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_monitors_test.py
mock_reader = test.mock.MagicMock()
monitor = debug_events_monitors.InfNanMonitor(mock_reader)
execution_digest = debug_events_reader.ExecutionDigest(
    1234, 1, "FooOp", output_tensor_device_ids=[0, 1])
execution = debug_events_reader.Execution(
    execution_digest,
    "worker01", ["a1", "b2", "e3"],
    debug_event_pb2.TensorDebugMode.CURT_HEALTH,
    graph_id=None,
    input_tensor_ids=[12, 34],
    output_tensor_ids=[56, 78],
    debug_tensor_values=[[-1, 0], [-1, 1]])  # [tensor_id, any_inf_nan].
monitor.on_execution(50, execution)

self.assertLen(monitor.alerts(), 1)
alert = monitor.alerts()[0]
self.assertEqual(alert.wall_time, 1234)
self.assertEqual(alert.op_type, "FooOp")
self.assertEqual(alert.output_slot, 1)
# The four fields below are unavailable under CURT_HEALTH mode by design.
self.assertIsNone(alert.size)
self.assertIsNone(alert.num_neg_inf)
self.assertIsNone(alert.num_pos_inf)
self.assertIsNone(alert.num_nan)
self.assertEqual(alert.execution_index, 50)
self.assertIsNone(alert.graph_execution_trace_index)
