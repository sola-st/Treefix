import unittest # pragma: no cover

class MockSession:# pragma: no cover
    def __enter__(self):# pragma: no cover
        return self# pragma: no cover
    def __exit__(self, exc_type, exc_value, traceback):# pragma: no cover
        pass # pragma: no cover
class MyTestCase(unittest.TestCase):# pragma: no cover
    def cached_session(self):# pragma: no cover
        return MockSession() # pragma: no cover
self = MyTestCase() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Testing name scope requires placeholders and a graph.
from l3.Runtime import _l_
with ops.Graph().as_default():
    _l_(16403)

    with self.cached_session():
        _l_(16402)

        single_image = array_ops.placeholder(dtypes.float32, shape=[50, 60, 3])
        _l_(16399)
        y = image_ops.resize_images(single_image, [55, 66])
        _l_(16400)
        self.assertTrue(y.op.name.startswith("resize"))
        _l_(16401)
