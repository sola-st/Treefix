# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_split_op_test.py
# Test case for GitHub issue 53660.
axis = [1, 2]
with self.assertRaisesRegexp(errors.InvalidArgumentError,
                             r'axis should be a scalar'):
    self.evaluate(
        sparse_ops.sparse_split(
            sp_input=self._SparseTensor_4x6(), num_split=3, axis=axis))
