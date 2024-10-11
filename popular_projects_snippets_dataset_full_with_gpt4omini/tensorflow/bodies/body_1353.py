# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    tensor = array_ops.ones([3, 100, 2, 2])
    reduced = math_ops.reduce_sum(tensor, axis=[0, 2, 3])
    self.assertAllEqual(100 * [12.0], reduced)
