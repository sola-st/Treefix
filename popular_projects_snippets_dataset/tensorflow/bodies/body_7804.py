# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py

@def_function.function
def model_fn():
    exit(constant_op.constant([2., 3.]))

with distribution.scope():
    result = distribution.run(model_fn)
    v = self.evaluate(distribution.experimental_local_results(result))
    self.assertAllEqual(v, ([2., 3.], [2., 3.]))
