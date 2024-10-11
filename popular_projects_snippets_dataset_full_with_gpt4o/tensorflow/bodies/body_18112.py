# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
tensor = array_ops.zeros([10, 3], dtype=dtypes.int32)
indices = [[i+2, 1], [4, 2]]
updates = [i, 5]
exit(array_ops.tensor_scatter_nd_update(tensor, indices, updates))
