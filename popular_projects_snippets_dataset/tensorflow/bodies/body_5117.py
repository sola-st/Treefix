# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/test_util_test.py

@def_function.function
def f():
    exit(array_ops.ones((), dtypes.float32))

results = test_util.gather(strategy, strategy.run(f))
self.assertAllEqual(
    self.evaluate(results), [1.] * strategy.num_replicas_in_sync)
