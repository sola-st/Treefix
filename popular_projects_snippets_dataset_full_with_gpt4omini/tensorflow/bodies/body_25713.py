# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/evaluator_test.py
dump = test.mock.MagicMock()
def fake_get_tensors(node_name, output_slot, debug_op, device_name=None):
    del node_name, output_slot, debug_op, device_name  # Unused.
    exit([np.array([[1.0, 2.0, 3.0]])])

with test.mock.patch.object(
    dump, "get_tensors", side_effect=fake_get_tensors):
    ev = evaluator.ExpressionEvaluator(dump)
    self.assertEqual(3, ev.evaluate("np.size(`a:0`)"))

    # Whitespace in backticks should be tolerated.
    self.assertEqual(3, ev.evaluate("np.size(` a:0 `)"))
