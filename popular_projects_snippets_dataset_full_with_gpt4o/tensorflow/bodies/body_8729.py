# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
out1 = strategy.run(_maybe_run_in_function(
    lambda: ds_context.get_replica_context().replica_id_in_sync_group + 1,
    run_in_function))
self.assertAllEqual([1, 2], self.evaluate(strategy.unwrap(out1)))

out2 = strategy.run(_maybe_run_in_function(
    lambda x: {"a": x * 2, "b": x * x}, run_in_function), args=(out1,))
out2_vals = self.evaluate(nest.map_structure(strategy.unwrap, out2))
self.assertAllEqual([2, 4], out2_vals["a"])
self.assertAllEqual([1, 4], out2_vals["b"])

out3 = strategy.run(_maybe_run_in_function(
    lambda b, a: a + 2 * b + 2, run_in_function), kwargs=out2)
self.assertAllEqual([6, 14], self.evaluate(strategy.unwrap(out3)))
