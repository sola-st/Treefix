# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_monitors_test.py
alert = debug_events_monitors.InfNanAlert(
    1234,
    "FooOp",
    1,
    size=1000,
    num_neg_inf=5,
    num_pos_inf=10,
    num_nan=20,
    execution_index=777,
    graph_execution_trace_index=888)
self.assertEqual(alert.wall_time, 1234)
self.assertEqual(alert.op_type, "FooOp")
self.assertEqual(alert.output_slot, 1)
self.assertEqual(alert.size, 1000)
self.assertEqual(alert.num_neg_inf, 5)
self.assertEqual(alert.num_pos_inf, 10)
self.assertEqual(alert.num_nan, 20)
self.assertEqual(alert.execution_index, 777)
self.assertEqual(alert.graph_execution_trace_index, 888)
