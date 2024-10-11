# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
np.random.seed(123)
inputs = constant_op.constant(
    np.random.normal(0.0, 1.0, 8 * 9 * 10).reshape([8, 9, 10]),
    dtype=dtypes.float32)

expected_result = gen_linalg_ops.qr(
    input=inputs, full_matrices=True, name=None)

if shard_type == 'replicated':
    layout = self.first_dimension_sharded_layout_3d
else:
    layout = self.replicated_layout_3d

inputs = numpy_util.pack_numpy(inputs, layout)

got = gen_linalg_ops.qr(
    input=inputs, full_matrices=full_matrices, name=None)
self.assertDTensorEqual(expected_result[0], layout, got[0])
self.assertDTensorEqual(expected_result[1], layout, got[1])
