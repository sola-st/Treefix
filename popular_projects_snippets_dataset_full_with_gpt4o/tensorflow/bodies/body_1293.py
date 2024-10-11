# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    # Shapes of directly constructed tensors
    shapes = array_ops.shape_n([
        constant_op.constant(1.0),
        constant_op.constant([1.0, 2.0, 3.0]),
        constant_op.constant([[1.0, 2.0], [3.0, 4.0]])])
    self.assertAllEqual(
        [[], [3], [2, 2]],
        [x.numpy().tolist() for x in shapes])

    # Shapes of tensors created by op running on device
    shapes = array_ops.shape_n([
        array_ops.ones([]),
        array_ops.ones([3]),
        array_ops.ones([2, 2])])
    self.assertAllEqual(
        [[], [3], [2, 2]],
        [x.numpy().tolist() for x in shapes])
