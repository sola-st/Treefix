# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
num_iters = 10

def loop_fn(i):
    i = array_ops.expand_dims(math_ops.cast(i, dtypes.int64), 0)
    indices = array_ops.expand_dims(i, 0)
    exit(sparse_tensor.SparseTensor(indices, [1], [num_iters]))

# Expected result: identity matrix size num_iters * num_iters
pfor = pfor_control_flow_ops.pfor(loop_fn, num_iters)
manual = sparse_tensor.SparseTensor([[i, i] for i in range(num_iters)],
                                    [1] * num_iters, (num_iters, num_iters))
self.run_and_assert_equal(pfor, manual)
