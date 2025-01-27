# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
layout = (
    self.replicated_layout_2d
    if shard_type == 'replicated' else self.first_dimension_sharded_layout)

a = constant_op.constant([[True, False], [False, True]])
b = constant_op.constant([[10., 20.], [30., 40.]])
c = constant_op.constant([[50., 60.], [70., 80.]])
expected_result = op(a, b, c)

if shard_type == 'replicated':
    a = api.copy_to_mesh(a, layout)
    b = api.copy_to_mesh(b, layout)
    c = api.copy_to_mesh(c, layout)
else:
    a = numpy_util.pack_numpy(a, layout)
    b = numpy_util.pack_numpy(b, layout)
    c = numpy_util.pack_numpy(c, layout)
dtensor_result = op(a, b, c)

self.assertDTensorEqual(expected_result, layout, dtensor_result)
