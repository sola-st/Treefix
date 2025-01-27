# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/evaluator_test.py
dump = test.mock.MagicMock()
ev = evaluator.ExpressionEvaluator(dump)
with self.assertRaisesRegex(ValueError,
                            r".* tensor name .* expression .* malformed"):
    ev.evaluate("np.matmul(`a`, `b`)")

with self.assertRaisesRegex(ValueError,
                            r".* tensor name .* expression .* malformed"):
    ev.evaluate("np.matmul(`a:0:DebugIdentity:0`, `b:1:DebugNanCount:2`)")

with self.assertRaises(ValueError):
    ev.evaluate("np.matmul(`a:0[]`, `b:0[]`)")
