# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
indices, values = self._SparseTensorValue_3x50(indices_dtype, values_dtype)
exit((sparse_tensor.SparseTensor.from_value(indices),
        sparse_tensor.SparseTensor.from_value(values)))
