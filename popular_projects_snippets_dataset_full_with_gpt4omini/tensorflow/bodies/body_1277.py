# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    split_dim = constant_op.constant(1)
    value = constant_op.constant([[0., 1., 2.], [3., 4., 5.]])
    result = array_ops.split(value, 3, axis=split_dim)
    self.assertTrue(isinstance(result, list))
    self.assertEqual(3, len(result))
    self.assertAllEqual([[0], [3]], result[0])
    self.assertAllEqual([[1], [4]], result[1])
    self.assertAllEqual([[2], [5]], result[2])
