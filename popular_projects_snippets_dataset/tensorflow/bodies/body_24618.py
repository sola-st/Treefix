# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_monitors_test.py
mock_reader = test.mock.MagicMock()
mock_reader.execution_to_tensor_values.return_value = [
    np.array([[0.0, -1.0, 1.0]]),
    np.array(tensor_value, dtype=dtype)
]
monitor = debug_events_monitors.InfNanMonitor(mock_reader)
execution_digest = debug_events_reader.ExecutionDigest(
    1234,
    1,
    "__inference_bar_function_1234",
    output_tensor_device_ids=[0, 1])
execution = debug_events_reader.Execution(
    execution_digest,
    "worker01", ["a1", "b2", "e3"],
    debug_event_pb2.TensorDebugMode.FULL_TENSOR,
    graph_id=None,
    input_tensor_ids=[12, 34],
    output_tensor_ids=[56, 78])
monitor.on_execution(70, execution)

if expected_num_neg_inf or expected_num_pos_inf or expected_num_nan:
    self.assertLen(monitor.alerts(), 1)
    alert = monitor.alerts()[0]
    self.assertEqual(alert.wall_time, 1234)
    self.assertEqual(alert.op_type, "__inference_bar_function_1234")
    self.assertEqual(alert.output_slot, 1)
    self.assertEqual(alert.size, expected_size)
    self.assertEqual(alert.num_neg_inf, expected_num_neg_inf)
    self.assertEqual(alert.num_pos_inf, expected_num_pos_inf)
    self.assertEqual(alert.num_nan, expected_num_nan)
    self.assertEqual(alert.execution_index, 70)
    self.assertIsNone(alert.graph_execution_trace_index, 70)
else:
    self.assertEmpty(monitor.alerts())
