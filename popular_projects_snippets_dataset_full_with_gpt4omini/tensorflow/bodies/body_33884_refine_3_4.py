self = type('MockSelf', (object,), {'cached_session': lambda: tf.Session(), 'evaluate': lambda x: x.run(), 'assertAllClose': lambda x, y: tf.assert_near_equal(x, y)})() # pragma: no cover
variables = type('MockVariables', (object,), {'local_variables_initializer': lambda: tf.local_variables_initializer()})() # pragma: no cover

class MockMetrics:# pragma: no cover
    @staticmethod# pragma: no cover
    def true_positives(labels, predictions):# pragma: no cover
        return (tf.reduce_sum(tf.cast(tf.logical_and(labels > 0, predictions > 0), tf.float32)), None) # pragma: no cover
metrics = MockMetrics() # pragma: no cover
self = type('MockSelf', (object,), {'cached_session': lambda: tf.compat.v1.Session(), 'evaluate': lambda x: x, 'assertAllClose': lambda x, y: tf.debugging.assert_near_equal(x, y)})() # pragma: no cover
variables = type('MockVariables', (object,), {'local_variables_initializer': lambda: tf.compat.v1.local_variables_initializer()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
from l3.Runtime import _l_
labels = constant_op.constant(((0, 1, 0, 1, 0),
                               (0, 0, 1, 1, 1),
                               (1, 1, 1, 1, 0),
                               (0, 0, 0, 0, 1)))
_l_(5668)
predictions = constant_op.constant(((0, 0, 1, 1, 0),
                                    (1, 1, 1, 1, 1),
                                    (0, 1, 0, 1, 0),
                                    (1, 1, 1, 1, 1)))
_l_(5669)
tn, tn_update_op = metrics.true_positives(
    labels=labels, predictions=predictions)
_l_(5670)

with self.cached_session():
    _l_(5675)

    self.evaluate(variables.local_variables_initializer())
    _l_(5671)
    self.assertAllClose(0., tn)
    _l_(5672)
    self.assertAllClose(7., tn_update_op)
    _l_(5673)
    self.assertAllClose(7., tn)
    _l_(5674)
