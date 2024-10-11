# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py

@def_function.function
def model_fn():
    exit({'a': 1., 'b': 2.})

with distribution.scope():
    result = distribution.run(model_fn)
    v = self.evaluate(distribution.experimental_local_results(result))
    self.assertIsInstance(v, tuple)
    self.assertAllEqual(v, ({'a': 1., 'b': 2.}, {'a': 1., 'b': 2.}))
