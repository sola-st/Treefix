import numpy as np # pragma: no cover

class MockSession: # pragma: no cover
    def __enter__(self): return tf.compat.v1.Session().__enter__() # pragma: no cover
    def __exit__(self, *args): return tf.compat.v1.Session().__exit__(*args) # pragma: no cover
    def cached_session(self): return self # pragma: no cover
self = type('Mock', (object,), {'cached_session': MockSession().cached_session, 'assertTrue': lambda x: None})() # pragma: no cover

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
