class MockArrayOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def ones(shape): # pragma: no cover
        return tf.ones(shape) # pragma: no cover
 # pragma: no cover
class MockNNOps: # pragma: no cover
    @staticmethod # pragma: no cover
    def max_pool_v2(input, ksize, strides, padding): # pragma: no cover
        return tf.nn.max_pool2d(input, ksize, strides, padding) # pragma: no cover
 # pragma: no cover
    @staticmethod # pragma: no cover
    def max_pool1d(input, ksize, strides, padding): # pragma: no cover
        input_reshaped = tf.reshape(input, [1, input.shape[0], input.shape[1] * input.shape[2], 1]) # pragma: no cover
        result = tf.nn.max_pool2d(input_reshaped, [1, ksize, ksize, 1], [1, strides, strides, 1], padding) # pragma: no cover
        return tf.reshape(result, [input.shape[0], result.shape[1], -1]) # pragma: no cover
 # pragma: no cover
array_ops = MockArrayOps() # pragma: no cover
nn_ops = MockNNOps() # pragma: no cover
 # pragma: no cover
class SelfMock: # pragma: no cover
    @staticmethod # pragma: no cover
    def evaluate(tensor): # pragma: no cover
        return tensor.numpy() # pragma: no cover
 # pragma: no cover
    @classmethod # pragma: no cover
    def assertAllEqual(cls, a, b): # pragma: no cover
        assert (a == b).all(), f"{a} != {b}" # pragma: no cover
 # pragma: no cover
self = SelfMock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
from l3.Runtime import _l_
x = array_ops.ones([3, 6, 5])
_l_(17657)
ksize = 2
_l_(17658)
strides = 2
_l_(17659)

y1 = nn_ops.max_pool_v2(x, ksize, strides, "SAME")
_l_(17660)
y2 = nn_ops.max_pool1d(x, ksize, strides, "SAME")
_l_(17661)

self.assertAllEqual(self.evaluate(y1), self.evaluate(y2))
_l_(17662)
