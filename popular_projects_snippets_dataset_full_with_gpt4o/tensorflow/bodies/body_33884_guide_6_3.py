def true_positives(labels, predictions): # pragma: no cover
    return tf.reduce_sum(tf.cast(tf.logical_and(tf.equal(labels, 1), tf.equal(predictions, 1)), tf.float32)) # pragma: no cover
 # pragma: no cover
metrics = type('MockMetrics', (object,), {'true_positives': true_positives}) # pragma: no cover
 # pragma: no cover
class MockSession: # pragma: no cover
    def __enter__(self): # pragma: no cover
        self.sess = Session() # pragma: no cover
        return self.sess # pragma: no cover
    def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
        self.sess.close() # pragma: no cover
    def evaluate(self, tensor): # pragma: no cover
        return self.sess.run(tensor) # pragma: no cover
    def assertAllClose(self, actual, expected, rtol=1e-05, atol=1e-08): # pragma: no cover
        np.testing.assert_allclose(actual, expected, rtol=rtol, atol=atol) # pragma: no cover
 # pragma: no cover
class Self: # pragma: no cover
    def cached_session(self): # pragma: no cover
        return MockSession() # pragma: no cover
 # pragma: no cover
self = Self() # pragma: no cover

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
