# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
trace_digest = debug_events_reader.GraphExecutionTraceDigest(
    1234, 5678, "FooOp", "Model_1/Foo_2", 1, "deadbeef")
trace = debug_events_reader.GraphExecutionTrace(
    trace_digest, ["g1", "g2", "deadbeef"],
    debug_event_pb2.TensorDebugMode.CURT_HEALTH,
    debug_tensor_value=[3, 1], device_name="/device:GPU:0")
json = trace.to_json()
self.assertEqual(json["wall_time"], 1234)
self.assertEqual(json["op_type"], "FooOp")
self.assertEqual(json["op_name"], "Model_1/Foo_2")
self.assertEqual(json["output_slot"], 1)
self.assertEqual(json["graph_id"], "deadbeef")
self.assertEqual(json["graph_ids"], ("g1", "g2", "deadbeef"))
self.assertEqual(json["tensor_debug_mode"],
                 debug_event_pb2.TensorDebugMode.CURT_HEALTH)
self.assertEqual(json["debug_tensor_value"], (3, 1))
self.assertEqual(json["device_name"], "/device:GPU:0")
