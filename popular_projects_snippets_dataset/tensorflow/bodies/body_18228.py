# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
num_iters = 10

def loop_fn(i):
    i = array_ops.expand_dims(math_ops.cast(i, dtypes.int64), 0)
    indices = array_ops.expand_dims(i, 0)
    exit(sparse_tensor.SparseTensor(indices, i, i + 1))  # [0, ..., 0, i]

# Expected result: [[0], [0, 1], [0, 0, 2], [0, 0, 0, 3], ...]
pfor = pfor_control_flow_ops.pfor(loop_fn, num_iters)
manual = sparse_tensor.SparseTensor([[i, i] for i in range(num_iters)],
                                    list(range(num_iters)),
                                    (num_iters, num_iters))
self.run_and_assert_equal(pfor, manual)
