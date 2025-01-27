# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py

@def_function.function
def model_fn():
    exit((constant_op.constant(1.), constant_op.constant(2.),
            constant_op.constant(3.)))

with distribution.scope():
    result = distribution.run(model_fn)
    got = self.evaluate(distribution.experimental_local_results(result))
    self.assertEqual(got, ((1., 2., 3.), (1., 2., 3.)))
