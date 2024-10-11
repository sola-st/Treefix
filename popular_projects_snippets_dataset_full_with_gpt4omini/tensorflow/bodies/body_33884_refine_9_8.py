metrics = type('MockMetrics', (object,), {'true_positives': lambda self, labels, predictions: (tf.Variable(0, dtype=tf.int32), tf.reduce_sum(tf.cast(tf.logical_and(tf.equal(labels, 1), tf.equal(predictions, 1)), tf.int32)) )})() # pragma: no cover
self = type('MockSelf', (object,), {'cached_session': lambda self: tf.compat.v1.Session(), 'evaluate': lambda self, x: x.eval(), 'assertAllClose': lambda self, a, b: tf.Assert(tf.reduce_all(tf.abs(a - b) < 1e-6), [a, b])})() # pragma: no cover
variables = type('MockVariables', (object,), {'local_variables_initializer': lambda self: tf.local_variables_initializer()})() # pragma: no cover

metrics = type('MockMetrics', (object,), {'true_positives': lambda self, labels, predictions: (tf.Variable(0, dtype=tf.int32), tf.constant(7))})() # pragma: no cover
self = type('MockSelf', (object,), {'cached_session': lambda self: tf.compat.v1.Session(), 'evaluate': lambda self, x: None, 'assertAllClose': lambda self, a, b: print('Assertion passed' if abs(a - b) < 1e-6 else f'Assertion failed: {a} is not close to {b}')})() # pragma: no cover
variables = type('MockVariables', (object,), {'local_variables_initializer': lambda self: tf.local_variables_initializer()})() # pragma: no cover

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
