# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/evaluator_test.py
dump = test.mock.MagicMock()
def fake_get_tensors(node_name, output_slot, debug_op, device_name=None):
    del node_name, output_slot, debug_op, device_name  # Unused.
    raise debug_data.WatchKeyDoesNotExistInDebugDumpDirError()

with test.mock.patch.object(
    dump, "get_tensors", side_effect=fake_get_tensors):
    ev = evaluator.ExpressionEvaluator(dump)
    with self.assertRaisesRegex(
        ValueError, "Eval failed due to the value of .* being unavailable"):
        ev.evaluate("np.matmul(`a:0`, `b:0`)")
