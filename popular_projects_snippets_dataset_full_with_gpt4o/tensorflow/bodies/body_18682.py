# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
init = init_ops_v2.constant_initializer((10, 20, 30))
tensor = init(shape=[3])
self.assertAllEqual(self.evaluate(tensor), [10, 20, 30])
self.assertEqual(tensor.shape, [3])
