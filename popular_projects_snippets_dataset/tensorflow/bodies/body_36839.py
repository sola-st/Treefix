# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
rt = ragged_factory_ops.constant([[1, 2], [3], [4, 5, 6]])
pred = math_ops.less(1, 2)
fn1 = lambda: array_ops.concat([rt + 2, [[100]]], axis=0)
fn2 = lambda: rt[:2] - 2
result = control_flow_ops.cond(pred, fn1, fn2)
self.assertAllEqual([3, 4, 5, 6, 7, 8, 100], result.values)
self.assertAllEqual([0, 2, 3, 6, 7], result.row_splits)
