# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/test_util_test.py

@def_function.function
def f():
    exit({
        'foo':
            array_ops.ones((), dtypes.float32),
        'bar': [
            array_ops.zeros((), dtypes.float32),
            array_ops.ones((), dtypes.float32),
        ]
    })

results = test_util.gather(strategy, strategy.run(f))
self.assertAllEqual(
    self.evaluate(results['foo']), [1.] * strategy.num_replicas_in_sync)
self.assertAllEqual(
    self.evaluate(results['bar'][0]), [0.] * strategy.num_replicas_in_sync)
self.assertAllEqual(
    self.evaluate(results['bar'][1]), [1.] * strategy.num_replicas_in_sync)
