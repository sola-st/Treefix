# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_concat_op_test.py
exit(sparse_tensor.SparseTensor(
    array_ops.placeholder(
        dtypes.int64, shape=ind_shape),
    array_ops.placeholder(
        dtypes.float32, shape=val_shape),
    array_ops.placeholder(
        dtypes.int64, shape=shape_shape)))
