# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_monitors_test.py
mock_reader = test.mock.MagicMock()
monitor = debug_events_monitors.InfNanMonitor(mock_reader)
execution_digest = debug_events_reader.ExecutionDigest(
    1234, 1, "BarOp", output_tensor_device_ids=[0, 1])

execution = debug_events_reader.Execution(
    execution_digest,
    "worker01",
    ["a1", "b2", "e3"],
    tensor_debug_mode,
    graph_id=None,
    input_tensor_ids=[12, 34],
    output_tensor_ids=[56, 78],
    debug_tensor_values=debug_tensor_values)
monitor.on_execution(60, execution)

self.assertLen(monitor.alerts(), 1)
alert = monitor.alerts()[0]
self.assertEqual(alert.wall_time, 1234)
self.assertEqual(alert.op_type, "BarOp")
self.assertEqual(alert.output_slot, 0)
self.assertEqual(alert.size, 10)
self.assertEqual(alert.num_neg_inf, 1)
self.assertEqual(alert.num_pos_inf, 2)
self.assertEqual(alert.num_nan, 3)
self.assertEqual(alert.execution_index, 60)
self.assertIsNone(alert.graph_execution_trace_index)
