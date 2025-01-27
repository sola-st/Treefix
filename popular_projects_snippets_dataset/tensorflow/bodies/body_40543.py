# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
x = constant_op.constant([1, 2, 3, 4, 5, 6])
y = constant_op.constant([1, 3, 5])
result = array_ops.listdiff(x, y)
out, idx = result
self.assertIs(out, result.out)
self.assertIs(idx, result.idx)
self.assertAllEqual([2, 4, 6], out)
self.assertAllEqual([1, 3, 5], idx)
