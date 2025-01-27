# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
values = constant_op.constant([2.0, 4.0], name="values")
indices = constant_op.constant([[0], [3]],
                               dtype=dtypes.int64,
                               name="indices")
shape = constant_op.constant([10], dtype=dtypes.int64, name="dense_shape")
x = sparse_tensor.SparseTensor(indices, values, dense_shape=shape)
pred = math_ops.less(1, 2)
fn1 = lambda: sparse_tensor.SparseTensor(
    indices + 1, x.values + 1, dense_shape=shape)
fn2 = lambda: sparse_tensor.SparseTensor(
    indices, x.values - 1, dense_shape=shape)
r = control_flow_ops.cond(pred, fn1, fn2)
self.assertAllEqual([3.0, 5.0], r.values)
self.assertAllEqual([[1], [4]], r.indices)
self.assertAllEqual(r.values.get_shape(), (2,))
