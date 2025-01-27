# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
out1 = strategy.run(lambda: array_ops.identity(4.))
self.assertAllEqual([4.], self.evaluate(strategy.unwrap(out1)))

out2 = strategy.run(lambda x: {"a": x * 2, "b": x * x}, args=(out1,))
out2_vals = self.evaluate(nest.map_structure(strategy.unwrap, out2))
self.assertAllEqual([8.], out2_vals["a"])
self.assertAllEqual([16.], out2_vals["b"])

out3 = strategy.run(lambda b, a: a + 2 * b + 2, kwargs=out2)
self.assertAllEqual([42.], self.evaluate(strategy.unwrap(out3)))
