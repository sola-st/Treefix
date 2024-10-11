# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/batch_test.py
exit(sparse_tensor.SparseTensorValue(
    indices=array_ops.expand_dims(
        math_ops.range(i, dtype=dtypes.int64), 1),
    values=array_ops.fill([math_ops.cast(i, dtypes.int32)], i),
    dense_shape=[i]))
