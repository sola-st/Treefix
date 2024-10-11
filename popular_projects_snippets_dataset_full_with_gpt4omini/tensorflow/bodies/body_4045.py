# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
for axis, expected_layout in [([0], self.replicated_layout_1d),
                              ([1], self.replicated_layout_1d),
                              ([0, 1], self.scalar_replicated_layout),
                              (None, self.scalar_replicated_layout)]:
    # Disable the pylint as the cell var is used for this iteration only.
    # pylint: disable=cell-var-from-loop
    reduction_op = lambda x: op(x, axis=axis)
    # pylint: enable=cell-var-from-loop

    a = constant_op.constant([[1., 2.], [3., 4.]])
    expected_result = reduction_op(a)

    a = api.copy_to_mesh(a, self.replicated_layout_2d)
    with api.run_on(self.mesh):
        dtensor_result = reduction_op(a)

    self.assertDTensorEqual(expected_result, expected_layout, dtensor_result)
