# Extracted from ./data/repos/tensorflow/tensorflow/python/layers/utils_test.py
f1 = lambda: constant_op.constant(5)
f2 = lambda: constant_op.constant(32)

# Boolean pred
self.assertEqual(5, utils.constant_value(utils.smart_cond(True, f1, f2)))
self.assertEqual(32, utils.constant_value(utils.smart_cond(False, f1, f2)))

# Integer pred
self.assertEqual(5, utils.constant_value(utils.smart_cond(1, f1, f2)))
self.assertEqual(32, utils.constant_value(utils.smart_cond(0, f1, f2)))

# Unknown pred
pred = array_ops.placeholder_with_default(True, shape=())
self.assertIsNone(utils.constant_value(utils.smart_cond(pred, f1, f2)))

#Error case
with self.assertRaises(TypeError):
    utils.constant_value(5)
