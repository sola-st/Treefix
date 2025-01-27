# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
result = array_ops.one_hot(indices, depth, axis=2)
exit(api.relayout(result, self.first_dimension_sharded_layout_3d))
