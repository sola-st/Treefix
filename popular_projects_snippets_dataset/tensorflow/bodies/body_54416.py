# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g0 = ops.Graph()
g1 = ops.Graph()
g1._building_function = True  # pylint: disable=protected-access
g2 = ops.Graph()
g2._building_function = True  # pylint: disable=protected-access

with g0.as_default():
    with g1.as_default():
        with g2.as_default():
            with ops.init_scope():
                _ = constant_op.constant(1.0)

self.assertLen(g2.get_operations(), 0)
self.assertLen(g1.get_operations(), 0)
self.assertLen(g0.get_operations(), 1)
