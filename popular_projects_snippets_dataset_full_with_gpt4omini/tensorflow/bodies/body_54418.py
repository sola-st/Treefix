# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g0 = ops.Graph()
g1 = ops.Graph()
g1._building_function = True  # pylint: disable=protected-access
g2 = ops.Graph()
g2._building_function = True  # pylint: disable=protected-access
g3 = ops.Graph()
g3._building_function = False  # pylint: disable=protected-access

with g0.as_default():
    with g1.as_default():
        with ops.init_scope():
            # This op should be lifted into g0.
            _ = constant_op.constant(1.0)
            self.assertIs(g0, ops.get_default_graph())
            self.assertLen(g2.get_operations(), 0)
            self.assertLen(g1.get_operations(), 0)
            self.assertLen(g0.get_operations(), 1)
        with g2.as_default():
            with ops.init_scope():
                # This op should be lifted into g0.
                _ = constant_op.constant(1.0)
                self.assertIs(g0, ops.get_default_graph())
                with g3.as_default():
                    with ops.init_scope():
                        # This op should be lifted into g3, because g3 is not building a
                        # function.
                        _ = constant_op.constant(1.0)
                        self.assertIs(g3, ops.get_default_graph())

self.assertLen(g3.get_operations(), 1)
self.assertLen(g2.get_operations(), 0)
self.assertLen(g1.get_operations(), 0)
self.assertLen(g0.get_operations(), 2)
