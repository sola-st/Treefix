# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
indices_layout = Layout(indices_spec, self.mesh)
updates_layout = Layout(updates_spec, self.mesh)
indices = constant_op.constant([[0], [15]])
updates = constant_op.constant([[[5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7],
                                 [8, 8, 8, 8]],
                                [[5, 5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7],
                                 [8, 8, 8, 8]]])
shape = [16, 4, 4]

expected_result = gen_array_ops.scatter_nd(indices, updates, shape)
got_result = gen_array_ops.scatter_nd(
    numpy_util.pack_numpy(indices, indices_layout),
    numpy_util.pack_numpy(updates, updates_layout), shape)

self.assertDTensorEqual(expected_result, updates_layout, got_result)
