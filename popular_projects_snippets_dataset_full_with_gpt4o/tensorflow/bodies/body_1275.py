# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    empty = constant_op.constant([], dtype=dtypes.float32)
    result = array_ops.unstack(empty, 0)
    self.assertTrue(isinstance(result, list))
    self.assertEqual(0, len(result))
