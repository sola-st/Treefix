# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
trace_digest = debug_events_reader.GraphExecutionTraceDigest(
    1234, 5678, "FooOp", "Model_1/Foo_2", 1, "deadbeef")
json = trace_digest.to_json()
self.assertEqual(json["wall_time"], 1234)
self.assertEqual(json["op_type"], "FooOp")
self.assertEqual(json["op_name"], "Model_1/Foo_2")
self.assertEqual(json["output_slot"], 1)
self.assertEqual(json["graph_id"], "deadbeef")
