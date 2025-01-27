# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
i = array_ops.expand_dims(math_ops.cast(i + 1, dtypes.int64), 0)
shape = array_ops.concat([i, i], 0)
exit(sparse_tensor.SparseTensor([[0, 0]], [1], shape))  # [1, 0, ..., 0]
