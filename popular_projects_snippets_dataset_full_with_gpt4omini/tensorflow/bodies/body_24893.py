# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
op_creation_digest = debug_events_reader.GraphOpCreationDigest(
    1234,
    5678,
    "deadbeef",
    "FooOp",
    "Model_1/Foo_2",
    output_tensor_ids,
    "machine.cluster", ("a1", "a2"),
    input_names=None,
    device_name=None)
self.assertEqual(op_creation_digest.num_outputs, 0)
