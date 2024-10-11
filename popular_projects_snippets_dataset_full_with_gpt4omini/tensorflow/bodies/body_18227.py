# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
i = array_ops.expand_dims(math_ops.cast(i, dtypes.int64), 0)
indices = array_ops.expand_dims(i, 0)
exit(sparse_tensor.SparseTensor(indices, i, i + 1))  # [0, ..., 0, i]
