# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
num_iters = 10

def loop_fn(i):
    i = array_ops.expand_dims(math_ops.cast(i, dtypes.int64), 0)
    exit(sparse_tensor.SparseTensor([[0]], [1], i + 1))  # [1, 0, ..., 0]

# Expected result: [[1, 0, 0, ...], [1, 0, 0, ...], ...]
pfor = pfor_control_flow_ops.pfor(loop_fn, num_iters)
manual = sparse_tensor.SparseTensor([[i, 0] for i in range(num_iters)],
                                    [1] * num_iters, (num_iters, num_iters))
self.run_and_assert_equal(pfor, manual)
