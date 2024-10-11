# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
# Test validation of invalid SparseTensors.  The SparseTensor constructor
# prevents us from creating invalid SparseTensors (eps. in eager mode),
# so we create valid SparseTensors and then modify them to be invalid.

st1 = sparse_tensor.SparseTensor([[0, 0]], [0], [2, 2])
st1._indices = array_ops.zeros([], dtypes.int64)
with self.assertRaisesRegex((errors.InvalidArgumentError, ValueError),
                            'Input indices should be a matrix'):
    self.evaluate(sparse_ops.sparse_cross([st1]))

st2 = sparse_tensor.SparseTensor([[0, 0]], [0], [2, 2])
st2._values = array_ops.zeros([], dtypes.int64)
with self.assertRaisesRegex((errors.InvalidArgumentError, ValueError),
                            'Input values should be a vector'):
    self.evaluate(sparse_ops.sparse_cross([st2]))

st3 = sparse_tensor.SparseTensor([[0, 0]], [0], [2, 2])
st3._dense_shape = array_ops.zeros([], dtypes.int64)
with self.assertRaisesRegex((errors.InvalidArgumentError, ValueError),
                            'Input shapes should be a vector'):
    self.evaluate(sparse_ops.sparse_cross([st3]))
