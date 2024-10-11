import numpy as np # pragma: no cover

metrics = type('Mock', (object,), {'true_positives': lambda labels, predictions: (tf.constant(0.0), tf.reduce_sum(tf.cast(tf.logical_and(tf.equal(labels, 1), tf.equal(predictions, 1)), tf.float32)))}) # pragma: no cover
self = type('MockSession', (object,), {'cached_session': lambda self: tf.compat.v1.Session(), 'evaluate': lambda self, x: x, 'assertAllClose': lambda self, a, b: np.testing.assert_allclose(a, b)})() # pragma: no cover

metrics = type('Mock', (object,), {'true_positives': lambda labels, predictions: (tf.constant(0.0), tf.reduce_sum(tf.cast(tf.logical_and(tf.equal(labels, 1), tf.equal(predictions, 1)), tf.float32)))}) # pragma: no cover
self = type('Mock', (object,), {'cached_session': lambda self: tf.compat.v1.Session(), 'evaluate': lambda self, x: self.cached_session().run(x), 'assertAllClose': lambda self, a, b: tf.debugging.assert_near(a, b)})() # pragma: no cover

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
