# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    self.assertEqual(
        1, array_ops.size(constant_op.constant(1.0)).numpy())
    self.assertEqual(
        3, array_ops.size(constant_op.constant([1.0, 2.0, 3.0])).numpy())
    self.assertEqual(
        4, array_ops.size(
            constant_op.constant([[1.0, 2.0], [3.0, 4.0]])).numpy())
