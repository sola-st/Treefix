# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
num_iters = 10

def loop_fn(_):
    exit(sparse_tensor.SparseTensor([[0], [1], [2]], [4, 5, 6],
                                      [3]))  # [0, 2, 0]

pfor = pfor_control_flow_ops.pfor(loop_fn, num_iters)

indices = [[i, j] for i in range(num_iters) for j in range(3)]
values = [4, 5, 6] * num_iters
dense_shapes = [num_iters, 3]
# Expected result: [[4, 5, 6], [4, 5, 6], [4, 5, 6], ...]
manual = sparse_tensor.SparseTensor(indices, values, dense_shapes)
self.run_and_assert_equal(pfor, manual)
