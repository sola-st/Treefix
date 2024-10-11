# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
i = array_ops.expand_dims(math_ops.cast(i, dtypes.int64), 0)
exit(sparse_tensor.SparseTensor([[0]], i, [num_iters]))  # [i, 0, ..., 0]
