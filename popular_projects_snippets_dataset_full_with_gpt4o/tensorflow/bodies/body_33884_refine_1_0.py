metrics = type('Mock', (object,), {'true_positives': lambda labels, predictions: (0.0, 7.0)})() # pragma: no cover
self = type('Mock', (object,), {'cached_session': lambda self: MockSession(), 'evaluate': lambda self, op: None, 'assertAllClose': lambda self, expected, actual: None})() # pragma: no cover
variables = type('Mock', (object,), {'local_variables_initializer': lambda: None})() # pragma: no cover

metrics = type('Mock', (object,), {'true_positives': lambda labels, predictions: (0.0, tf.reduce_sum(tf.cast(tf.logical_and(tf.equal(labels, 0), tf.equal(predictions, 0)), tf.float32)).numpy())}) # pragma: no cover
self = type('Mock', (object,), {'cached_session': lambda self: tf.compat.v1.Session().__enter__(), 'evaluate': lambda self, op: None, 'assertAllClose': lambda self, expected, actual: tf.debugging.assert_near(expected, actual)})() # pragma: no cover
variables = type('Mock', (object,), {'local_variables_initializer': lambda: tf.compat.v1.variables_initializer([tf.compat.v1.get_variable('tn', initializer=0.0), tf.compat.v1.get_variable('tn_update_op', initializer=7.0)])})() # pragma: no cover

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
