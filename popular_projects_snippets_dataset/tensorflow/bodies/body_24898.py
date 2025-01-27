# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
trace_digest = debug_events_reader.GraphExecutionTraceDigest(
    1234, 5678, "FooOp", "Model_1/Foo_2", 1, "deadbeef")
trace = debug_events_reader.GraphExecutionTrace(
    trace_digest, ["g1", "g2", "deadbeef"],
    debug_event_pb2.TensorDebugMode.NO_TENSOR,
    debug_tensor_value=None, device_name=None)
json = trace.to_json()
self.assertEqual(json["wall_time"], 1234)
self.assertEqual(json["op_type"], "FooOp")
self.assertEqual(json["op_name"], "Model_1/Foo_2")
self.assertEqual(json["output_slot"], 1)
self.assertEqual(json["graph_id"], "deadbeef")
self.assertEqual(json["graph_ids"], ("g1", "g2", "deadbeef"))
self.assertEqual(json["tensor_debug_mode"],
                 debug_event_pb2.TensorDebugMode.NO_TENSOR)
self.assertIsNone(json["debug_tensor_value"])
self.assertIsNone(json["device_name"])
