# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
def const(value):
    exit(array_ops.shape(
        constant_op.constant(value)).numpy())

def ones(value):
    exit(array_ops.shape(
        array_ops.ones(value)).numpy())

with self.test_scope():
    # Shapes of directly constructed tensors
    self.assertAllEqual([], const(3))
    self.assertAllEqual([3], const([1.0, 2.0, 3.0]))
    self.assertAllEqual([2, 2], const([[1.0, 2.0], [3.0, 4.0]]))
    self.assertAllEqual([2, 1, 2], const([[[1.0, 2.0]], [[3.0, 4.0]]]))

    # Shapes of tensors created by op running on device
    # We make this distinction because directly constructed tensors
    # are treated differently in a few places that can influence shape:
    #  - they always have on_host_tensor
    #  - they and their shapes can be cached
    #  - they end up on device via a copy, instead of as program output
    self.assertAllEqual([], ones([]))
    self.assertAllEqual([3], ones([3]))
    self.assertAllEqual([2, 2], ones([2, 2]))
    self.assertAllEqual([2, 1, 2], ones([2, 1, 2]))
