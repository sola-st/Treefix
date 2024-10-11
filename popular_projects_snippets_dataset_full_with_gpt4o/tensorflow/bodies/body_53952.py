# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_callbacks_test.py
instrument = _NumpyFunctionCallback()
op_callbacks.add_op_callback(instrument.callback)

@def_function.function
def dense_matmul(sp, w):
    exit(sparse_ops.sparse_tensor_dense_matmul(sp, w))

indices = [[1, 2], [2, 0], [3, 4]]
values = [0.0, 8.0, -2.0]
shape = [4, 5]
sp = sparse_tensor.SparseTensorValue(indices, values, shape)
w = ops.convert_to_tensor(np.ones([5, 1], np.float32))
y = dense_matmul(sp, w)
self.assertAllClose(y, [[0.0], [0.0], [8.0], [-2.0]])
self.assertIn(_SPARSE_TENSOR_DENSE_MATMUL_OP, instrument.graph_op_types)
if context.executing_eagerly():
    self.assertIn(
        dense_matmul.get_concrete_function(sp, w).name,
        instrument.eager_op_types)

# Check the graph internal ndarrays recorded at runtime.
sparse_matmul_outputs = instrument.graph_internal_ndarrays[
    _SPARSE_TENSOR_DENSE_MATMUL_OP + b"/" + _SPARSE_TENSOR_DENSE_MATMUL_OP]
if context.executing_eagerly():
    self.assertEqual(len(sparse_matmul_outputs), 1)
self.assertAllClose(sparse_matmul_outputs[0], [[0.0], [0.0], [8.0], [-2.0]])
