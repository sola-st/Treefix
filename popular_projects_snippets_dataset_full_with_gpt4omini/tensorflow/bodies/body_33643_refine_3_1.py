_enqueue_vector = lambda sess, queue, values: sess.run(queue.enqueue(values)) # pragma: no cover

class SelfMock: pass # pragma: no cover
self = SelfMock() # pragma: no cover
self.cached_session = lambda: tf.compat.v1.Session() # pragma: no cover
self.evaluate = lambda x: x # pragma: no cover
self.assertAllClose = lambda x, y: tf.test.TestCase().assertAllClose(x, y) # pragma: no cover
_enqueue_vector = lambda sess, queue, values: sess.run(queue.enqueue(tf.convert_to_tensor(values))) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
from l3.Runtime import _l_
with self.cached_session() as sess:
    _l_(6001)

    values_queue = data_flow_ops.FIFOQueue(
        4, dtypes=dtypes_lib.float32, shapes=(1, 2))
    _l_(5990)
    _enqueue_vector(sess, values_queue, [0, 1])
    _l_(5991)
    _enqueue_vector(sess, values_queue, [-4.2, 9.1])
    _l_(5992)
    _enqueue_vector(sess, values_queue, [6.5, 0])
    _l_(5993)
    _enqueue_vector(sess, values_queue, [-3.2, 4.0])
    _l_(5994)
    values = values_queue.dequeue()
    _l_(5995)

    mean, update_op = metrics.mean_tensor(values)
    _l_(5996)

    self.evaluate(variables.local_variables_initializer())
    _l_(5997)
    for _ in range(4):
        _l_(5999)

        self.evaluate(update_op)
        _l_(5998)
    self.assertAllClose([[-0.9 / 4., 3.525]], self.evaluate(mean))
    _l_(6000)
