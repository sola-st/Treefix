# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    self.assertEqual(
        0, array_ops.rank(constant_op.constant(1.0)).numpy())
    self.assertEqual(
        1, array_ops.rank(constant_op.constant([1.0, 2.0, 3.0])).numpy())
    self.assertEqual(
        2, array_ops.rank(
            constant_op.constant([[1.0, 2.0], [3.0, 4.0]])).numpy())
