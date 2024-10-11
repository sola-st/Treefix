# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py

# TODO(b/193471732): changed back to dtypes.int32 once it is fixed.
int_dtype = dtypes.int64 if self.mesh.device_type(
) == 'GPU' else dtypes.int32

targets_layout = Layout(targets_sharding, self.mesh)
predictions_layout = Layout(predictions_sharding, self.mesh)

targets = constant_op.constant([2, 2, 1, 0], dtype=int_dtype)
predictions = constant_op.constant([[0.1, 0.3, 0.2, 0.4],
                                    [0.1, 0.2, 0.3, 0.4],
                                    [0.3, 0.4, 0.1, 0.2],
                                    [0.1, 0.3, 0.4, 0.2]])
topk = constant_op.constant(2, dtype=int_dtype)

expected_output = nn_ops.in_top_k_v2(targets, predictions, k=topk)

targets = numpy_util.pack_numpy(targets, targets_layout)
predictions = numpy_util.pack_numpy(predictions, predictions_layout)

dtensor_output = nn_ops.in_top_k_v2(targets, predictions, k=topk)

expected_sharding = [layout_lib.UNSHARDED]
# Select the more sharded layout
if targets_sharding[0] != layout_lib.UNSHARDED:
    expected_sharding[0] = targets_sharding[0]
if predictions_sharding[0] != layout_lib.UNSHARDED:
    expected_sharding[0] = predictions_sharding[0]

expected_layout = Layout(expected_sharding, self.mesh)
self.assertDTensorEqual(expected_output, expected_layout, dtensor_output)
