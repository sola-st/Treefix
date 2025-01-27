# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/resource_variable_ops_test.py
with context.eager_mode(), ops.device("gpu:0"):
    v = resource_variable_ops.ResourceVariable(1, dtype=dtype)
    self.assertEqual("/job:localhost/replica:0/task:0/device:GPU:0", v.device)
    self.assertAllEqual(1, v.numpy())
    v.assign_add(1)
    self.assertAllEqual(2, v.numpy())
    v.assign_sub(1)
    self.assertAllEqual(1, v.numpy())
    v = resource_variable_ops.ResourceVariable([1, 2], dtype=dtype)
    self.evaluate(
        v.scatter_add(
            indexed_slices.IndexedSlices(
                indices=[1],
                values=constant_op.constant([2], dtype=dtype))))
    self.assertAllEqual([1, 4], v.numpy())
    self.evaluate(
        v.scatter_update(
            indexed_slices.IndexedSlices(
                indices=[1],
                values=constant_op.constant([5], dtype=dtype))))
    self.assertAllEqual([1, 5], v.numpy())
    self.evaluate(
        v.scatter_max(
            indexed_slices.IndexedSlices(
                indices=[0, 1],
                values=constant_op.constant([2, 2], dtype=dtype))))
    self.assertAllEqual([2, 5], v.numpy())
    self.evaluate(v.scatter_nd_add(indices=[[1]], updates=[2]))
    self.assertAllEqual([2, 7], v.numpy())
    self.evaluate(v.scatter_nd_update(indices=[[1]], updates=[2]))
    self.assertAllEqual([2, 2], v.numpy())
    self.evaluate(v.scatter_nd_max(indices=[[1]], updates=[3]))
    self.assertAllEqual([2, 3], v.numpy())
    self.assertAllEqual(v.gather_nd([1]), 3)
