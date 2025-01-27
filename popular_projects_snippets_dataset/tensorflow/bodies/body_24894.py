# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
op_creation_digest = debug_events_reader.GraphOpCreationDigest(
    1234,
    5678,
    "deadbeef",
    "FooOp",
    "Model_1/Foo_2", [135],
    "machine.cluster", ("a1", "a2"),
    input_names=None,
    device_name=None)
json = op_creation_digest.to_json()
self.jsonRoundTripCheck(json)
self.assertEqual(json["wall_time"], 1234)
self.assertEqual(json["graph_id"], "deadbeef")
self.assertEqual(json["op_type"], "FooOp")
self.assertEqual(json["op_name"], "Model_1/Foo_2")
self.assertEqual(json["output_tensor_ids"], (135,))
self.assertEqual(json["host_name"], "machine.cluster")
self.assertEqual(json["stack_frame_ids"], ("a1", "a2"))
self.assertIsNone(json["input_names"])
self.assertIsNone(json["device_name"])
