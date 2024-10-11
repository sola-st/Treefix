self = type('Mock', (), {'cached_session': lambda: tf.Session()})() # pragma: no cover

self = type('Mock', (), {'cached_session': lambda: tf.compat.v1.Session(), 'assertTrue': lambda condition: print('Assert:', condition)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Testing name scope requires placeholders and a graph.
from l3.Runtime import _l_
with ops.Graph().as_default():
    _l_(4841)

    with self.cached_session():
        _l_(4840)

        single_image = array_ops.placeholder(dtypes.float32, shape=[50, 60, 3])
        _l_(4837)
        y = image_ops.resize_images(single_image, [55, 66])
        _l_(4838)
        self.assertTrue(y.op.name.startswith("resize"))
        _l_(4839)
