class MockSession: # pragma: no cover
    def __enter__(self): # pragma: no cover
        self.sess = tf.Session() # pragma: no cover
        return self.sess # pragma: no cover
    def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
        self.sess.close() # pragma: no cover
        return False # pragma: no cover
 # pragma: no cover
def _enqueue_vector(sess, queue, vector): # pragma: no cover
    enqueue_op = queue.enqueue([vector]) # pragma: no cover
    sess.run(enqueue_op) # pragma: no cover
 # pragma: no cover
class MockObject: # pragma: no cover
    def cached_session(self): # pragma: no cover
        return MockSession() # pragma: no cover
    def evaluate(self, tensor_or_op): # pragma: no cover
        with self.cached_session() as sess: # pragma: no cover
            return sess.run(tensor_or_op) # pragma: no cover
    def assertAllClose(self, a, b): # pragma: no cover
        np.testing.assert_allclose(a, b, rtol=1e-6, atol=1e-6, err_msg=f'{a} is not close to {b}') # pragma: no cover
 # pragma: no cover
self = MockObject() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
from l3.Runtime import _l_
with self.cached_session() as sess:
    _l_(18039)

    values_queue = data_flow_ops.FIFOQueue(
        4, dtypes=dtypes_lib.float32, shapes=(1, 2))
    _l_(18028)
    _enqueue_vector(sess, values_queue, [0, 1])
    _l_(18029)
    _enqueue_vector(sess, values_queue, [-4.2, 9.1])
    _l_(18030)
    _enqueue_vector(sess, values_queue, [6.5, 0])
    _l_(18031)
    _enqueue_vector(sess, values_queue, [-3.2, 4.0])
    _l_(18032)
    values = values_queue.dequeue()
    _l_(18033)

    mean, update_op = metrics.mean_tensor(values)
    _l_(18034)

    self.evaluate(variables.local_variables_initializer())
    _l_(18035)
    for _ in range(4):
        _l_(18037)

        self.evaluate(update_op)
        _l_(18036)
    self.assertAllClose([[-0.9 / 4., 3.525]], self.evaluate(mean))
    _l_(18038)
