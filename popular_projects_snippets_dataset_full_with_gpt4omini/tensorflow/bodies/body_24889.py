# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_writer_test.py
execution = debug_events_reader.Execution(
    debug_events_reader.ExecutionDigest(1234, 5678, "FooOp"),
    "localhost", ("a1", "b2"),
    debug_event_pb2.TensorDebugMode.FULL_HEALTH,
    graph_id="abcd",
    input_tensor_ids=[13, 37],
    output_tensor_ids=output_tensor_ids,
    debug_tensor_values=None)
self.assertEqual(execution.num_outputs, 0)
