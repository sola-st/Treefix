# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/evaluator_test.py
dump = test.mock.MagicMock()
ev = evaluator.ExpressionEvaluator(dump)
with self.assertRaises(SyntaxError):
    ev.evaluate("np.matmul(`a:0`, `b:0`) + `b:0")
