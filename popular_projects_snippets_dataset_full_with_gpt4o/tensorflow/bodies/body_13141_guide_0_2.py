import unittest # pragma: no cover

class TestMaxPool(unittest.TestCase): # pragma: no cover
    def setUp(self): # pragma: no cover
        pass
    def assertAllEqual(self, y1, y2): # pragma: no cover
        self.assertTrue((y1 == y2).all()) # pragma: no cover
test = TestMaxPool() # pragma: no cover
test.setUp() # pragma: no cover

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
