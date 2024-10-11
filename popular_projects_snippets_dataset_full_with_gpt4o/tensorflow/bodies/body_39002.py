# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_serialization_ops_test.py
if dtype is None:
    dtype = dtypes.int32
exit(sparse_tensor_lib.SparseTensor(
    array_ops.placeholder(dtypes.int64),
    array_ops.placeholder(dtype), array_ops.placeholder(dtypes.int64)))
