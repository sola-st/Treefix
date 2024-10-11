# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
expanded = array_ops.expand_dims_v2(src, axis=-1)
exit(api.relayout(expanded, self.first_dimension_sharded_layout_3d))
