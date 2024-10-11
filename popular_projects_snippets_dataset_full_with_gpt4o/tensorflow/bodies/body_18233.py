# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
i = array_ops.expand_dims(math_ops.cast(i, dtypes.int64), 0)
exit(sparse_tensor.SparseTensor([[0]], [1], i + 1))  # [1, 0, ..., 0]
