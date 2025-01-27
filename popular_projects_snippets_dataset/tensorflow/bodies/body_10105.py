# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
values = constant_op.constant([2, 3, 5, 7, 0, -1], shape=[3, 2])
indices = constant_op.constant([0, 2, 5])
x = math_ops.scalar_mul(-3, indexed_slices.IndexedSlices(values, indices))
with test_util.device(use_gpu=True):
    self.assertAllEqual(
        self.evaluate(x.values), [[-6, -9], [-15, -21], [0, 3]])
    self.assertAllEqual(self.evaluate(x.indices), [0, 2, 5])
