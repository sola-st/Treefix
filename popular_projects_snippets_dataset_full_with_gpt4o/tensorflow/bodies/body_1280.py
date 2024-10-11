# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    self.assertAllEqual(2, array_ops.identity(2))
