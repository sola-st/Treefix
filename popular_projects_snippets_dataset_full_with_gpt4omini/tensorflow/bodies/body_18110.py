# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
tensor = array_ops.zeros([10, 3], dtype=dtypes.int32)
indices = [[i+2], [4]]
updates = [[1, i*2, 3], [i+4, i-5, 6]]
exit(array_ops.tensor_scatter_nd_update(tensor, indices, updates))
