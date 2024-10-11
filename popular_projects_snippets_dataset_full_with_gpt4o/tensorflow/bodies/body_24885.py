# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
execution_digest = debug_events_reader.ExecutionDigest(
    1234, 5678, "FooOp", output_tensor_device_ids=None)
json = execution_digest.to_json()
self.jsonRoundTripCheck(json)
self.assertEqual(json["wall_time"], 1234)
self.assertEqual(json["op_type"], "FooOp")
self.assertEqual(json["output_tensor_device_ids"], None)
