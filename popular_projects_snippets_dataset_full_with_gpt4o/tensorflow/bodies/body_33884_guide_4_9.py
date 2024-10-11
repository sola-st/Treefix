class MockSession: # pragma: no cover
    def __enter__(self): # pragma: no cover
        self.session = tf.compat.v1.Session() # pragma: no cover
        return self.session # pragma: no cover
    def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
        self.session.close() # pragma: no cover
    def evaluate(self, fetches): # pragma: no cover
        return self.session.run(fetches) # pragma: no cover
    def assertAllClose(self, actual, expected): # pragma: no cover
        np.testing.assert_allclose(actual, expected, rtol=1e-5, atol=1e-8) # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), {'cached_session': MockSession})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
from l3.Runtime import _l_
labels = constant_op.constant(((0, 1, 0, 1, 0),
                               (0, 0, 1, 1, 1),
                               (1, 1, 1, 1, 0),
                               (0, 0, 0, 0, 1)))
_l_(17426)
predictions = constant_op.constant(((0, 0, 1, 1, 0),
                                    (1, 1, 1, 1, 1),
                                    (0, 1, 0, 1, 0),
                                    (1, 1, 1, 1, 1)))
_l_(17427)
tn, tn_update_op = metrics.true_positives(
    labels=labels, predictions=predictions)
_l_(17428)

with self.cached_session():
    _l_(17433)

    self.evaluate(variables.local_variables_initializer())
    _l_(17429)
    self.assertAllClose(0., tn)
    _l_(17430)
    self.assertAllClose(7., tn_update_op)
    _l_(17431)
    self.assertAllClose(7., tn)
    _l_(17432)
