# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
self.skipForDeviceType(['TPU'], 'StringFormat not supported on TPU.')

np.random.seed(123)
inputs = constant_op.constant(
    np.random.normal(0.0, 1.0, 8 * 9 * 9).reshape([8, 9, 9, 1]),
    dtype=dtypes.float32)
expected_result = gen_string_ops.string_format(inputs=[inputs])

if shard_spec == 'sharded':
    layout = Layout.batch_sharded(self.mesh, _MESH_DIM_X, rank=4)
else:
    layout = Layout.replicated(self.mesh, rank=4)
inputs = numpy_util.pack_numpy(inputs, layout)
got = gen_string_ops.string_format(inputs=[inputs])

# Manually compare instead of assertDTensorEqual since outputs are strings.
self.assertEqual(
    api.fetch_layout(got), Layout.replicated(self.mesh, rank=0))
for got_tensor in api.unpack(got):
    self.assertEqual(expected_result, got_tensor)
