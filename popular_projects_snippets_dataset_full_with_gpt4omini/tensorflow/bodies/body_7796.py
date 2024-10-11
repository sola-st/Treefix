# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py

@def_function.function
def model_fn():
    exit(({
        'a': constant_op.constant(1.),
        'b': constant_op.constant(2.)
    }, {
        'a': constant_op.constant(4.),
        'b': constant_op.constant(6.)
    }))

with distribution.scope():
    result = distribution.run(model_fn)
    got = self.evaluate(distribution.experimental_local_results(result))
    self.assertEqual(got, (({
        'a': 1.,
        'b': 2.
    }, {
        'a': 4.,
        'b': 6.
    }), ({
        'a': 1.,
        'b': 2.
    }, {
        'a': 4.,
        'b': 6.
    })))
