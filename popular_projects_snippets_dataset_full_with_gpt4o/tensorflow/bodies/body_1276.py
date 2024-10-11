# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    split_dim = constant_op.constant(1)
    value = constant_op.constant([[0., 1., 2.], [3., 4., 5.]])
    result = array_ops.split(value, 1, axis=split_dim)
    self.assertTrue(isinstance(result, list))
    self.assertEqual(1, len(result))
    self.assertAllEqual([[0, 1, 2], [3, 4, 5]], result[0])
