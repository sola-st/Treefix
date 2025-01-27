# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
c = gen_array_ops.pack(values=[a, b], axis=-1)
exit(api.relayout(c, self.first_dimension_sharded_layout_3d))
