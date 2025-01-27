# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
execution_digest = debug_events_reader.ExecutionDigest(
    1234, 5678, "FooOp", output_tensor_device_ids=[1357])
execution = debug_events_reader.Execution(
    execution_digest,
    "localhost",
    ("a1", "b2"),
    debug_event_pb2.TensorDebugMode.FULL_HEALTH,
    graph_id="abcd",
    input_tensor_ids=[13, 37],
    output_tensor_ids=None,
    debug_tensor_values=None)
json = execution.to_json()
self.jsonRoundTripCheck(json)
self.assertEqual(json["wall_time"], 1234)
self.assertEqual(json["op_type"], "FooOp")
self.assertEqual(json["output_tensor_device_ids"], (1357,))
self.assertEqual(json["host_name"], "localhost")
self.assertEqual(json["stack_frame_ids"], ("a1", "b2"))
self.assertEqual(json["tensor_debug_mode"],
                 debug_event_pb2.TensorDebugMode.FULL_HEALTH)
self.assertEqual(json["graph_id"], "abcd")
self.assertEqual(json["input_tensor_ids"], (13, 37))
self.assertIsNone(json["output_tensor_ids"])
self.assertIsNone(json["debug_tensor_values"])
