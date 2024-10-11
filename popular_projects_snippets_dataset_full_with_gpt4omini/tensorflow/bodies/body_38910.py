# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
vocab_size = 50
indices_v, values_v = self._SparseTensorValue_3x50(np.int32, np.float32)
with test_util.force_cpu():
    for indices in (indices_v,
                    sparse_tensor.SparseTensor.from_value(indices_v)):
        for values in (values_v,
                       sparse_tensor.SparseTensor.from_value(values_v)):
            sp_output = sparse_ops.sparse_merge(indices, values, vocab_size)

            output = self.evaluate(sp_output)
            self._AssertResultsSorted(output, vocab_size)
