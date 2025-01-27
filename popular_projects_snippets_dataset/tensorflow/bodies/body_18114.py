# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
tensor = array_ops.zeros([5, 5])
indices = [
    [[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]],
    [[0, 4], [1, 3], [2, 2], [3, 1], [4, 0]],
]
updates = [
    [1, i, 1, 1, 1],
    [1, 1, i+2, 1, i-5],
]
exit(array_ops.tensor_scatter_nd_update(tensor, indices, updates))
