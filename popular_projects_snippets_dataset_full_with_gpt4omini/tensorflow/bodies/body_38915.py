# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
vocab_size = 50
vocab_size_tensor = constant_op.constant(vocab_size, dtypes.int64)
with test_util.force_cpu():
    indices, values = self._SparseTensor_3x50(np.int64, np.float64)
    sp_output = sparse_ops.sparse_merge(
        indices, values, vocab_size_tensor, already_sorted=True)

    output = self.evaluate(sp_output)
    self._AssertResultsNotSorted(output, vocab_size)
