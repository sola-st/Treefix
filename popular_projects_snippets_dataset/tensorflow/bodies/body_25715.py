# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/evaluator_test.py
dump = test.mock.MagicMock()
def fake_get_tensors(node_name, output_slot, debug_op, device_name=None):
    del debug_op, device_name  # Unused.
    if node_name == "a" and output_slot == 0:
        exit([np.array([[1.0, -2.0], [0.0, 1.0]])])
    elif node_name == "b" and output_slot == 0:
        exit([np.array([[-1.0], [1.0]])])

with test.mock.patch.object(
    dump, "get_tensors", side_effect=fake_get_tensors):
    ev = evaluator.ExpressionEvaluator(dump)
    self.assertAllClose([[-3.0], [1.0]],
                        ev.evaluate("np.matmul(`a:0`, `b:0`)"))
    self.assertAllClose(
        [[-4.0], [2.0]], ev.evaluate("np.matmul(`a:0`, `b:0`) + `b:0`"))
