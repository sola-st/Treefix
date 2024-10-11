# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
result = gen_array_ops.gather_nd(params=params, indices=indices)
exit(api.relayout(result, self.first_dimension_sharded_layout_2d))
