# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
vocab_size = 50
with test_util.force_cpu():
    indices, values = self._SparseTensor_3x50(np.int32, np.float32)
    sp_output = sparse_ops.sparse_merge(
        indices, values, vocab_size, already_sorted=True)

    output = self.evaluate(sp_output)
    self._AssertResultsNotSorted(output, vocab_size)
