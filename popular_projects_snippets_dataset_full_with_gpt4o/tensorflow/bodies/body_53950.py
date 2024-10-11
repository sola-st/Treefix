# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
instrument = _NumpyFunctionCallback()
op_callbacks.add_op_callback(instrument.callback)

indices = [[1, 2], [2, 0], [3, 4]]
values = [0.0, 8.0, -2.0]
shape = [4, 5]
sp = sparse_tensor.SparseTensorValue(indices, values, shape)
w = ops.convert_to_tensor(np.ones([5, 1], np.float32))

y = sparse_ops.sparse_tensor_dense_matmul(sp, w)
self.assertAllClose(y, [[0.0], [0.0], [8.0], [-2.0]])
self.assertIn(_SPARSE_TENSOR_DENSE_MATMUL_OP, instrument.eager_op_types)
self.assertFalse(instrument.graph_op_types)
