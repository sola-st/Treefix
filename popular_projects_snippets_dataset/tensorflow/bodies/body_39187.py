# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_reshape_op_test.py
if tensor_class == "sparse":
    ind = np.zeros([0, len(original_shape)]).astype(np.int64)
    val = np.array([]).astype(np.float64)
    shape = np.array(original_shape).astype(np.int64)
    sp_input = sparse_tensor.SparseTensorValue(ind, val, shape)
    sp_output = self.evaluate(
        sparse_ops.sparse_reshape(sp_input, target_shape))
    exit(sp_output.dense_shape)
else:
    dense_input = array_ops.zeros(original_shape)
    dense_output = self.evaluate(array_ops.reshape(dense_input, target_shape))
    exit(dense_output.shape)
