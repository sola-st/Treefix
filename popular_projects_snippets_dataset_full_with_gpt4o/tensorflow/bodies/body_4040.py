# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
layout_a = self.replicated_layout_2d
layout_b = self.replicated_layout_2d
layout_output = self.replicated_layout_2d

if shard_type == 'sharded':
    layout_a = self.first_dimension_sharded_layout
    layout_b = self.first_dimension_sharded_layout
    layout_output = self.first_dimension_sharded_layout
elif shard_type == 'mixed':
    layout_b = self.first_dimension_sharded_layout
    layout_output = self.first_dimension_sharded_layout

a = constant_op.constant([[1., 2.], [3., 4.]])
b = constant_op.constant([[1., 2.], [3., 4.]])
expected_result = op([a, b])

with api.run_on(self.mesh):
    a = numpy_util.pack_numpy(a, layout_a)
    b = numpy_util.pack_numpy(b, layout_b)
    c = op([a, b])

self.assertDTensorEqual(expected_result, layout_output, c)
