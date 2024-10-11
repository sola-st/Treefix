# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
inputs_layout = Layout(sharding, self.mesh)

inputs = constant_op.constant(
    np.random.uniform(size=[4, 16]), dtype=dtypes.float32)
topk = constant_op.constant(2, dtype=dtypes.int32)

expected_topk_values, expected_topk_indices = nn_ops.top_k(inputs, k=topk)

inputs = numpy_util.pack_numpy(inputs, inputs_layout)

dtensor_topk_values, dtensor_topk_indices = nn_ops.top_k(inputs, k=topk)

expected_sharding = [sharding[0], layout_lib.UNSHARDED]
expected_layout = Layout(expected_sharding, self.mesh)

self.assertDTensorEqual(expected_topk_values, expected_layout,
                        dtensor_topk_values)
self.assertDTensorEqual(expected_topk_indices, expected_layout,
                        dtensor_topk_indices)
