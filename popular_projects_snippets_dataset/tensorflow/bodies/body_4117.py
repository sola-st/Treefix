# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
for axis in [0, 1]:
    inputs = constant_op.constant([[1, 2, 3, 4], [5, 6, 7, 8]],
                                  dtype=dtypes.float32)
    expect_result = math_ops.argmax_v2(
        inputs, axis=axis, output_type=dtypes.int32)

    input_layout = Layout(sharding, self.mesh)
    inputs = numpy_util.pack_numpy(inputs.numpy(), input_layout)

    output_layout = Layout([sharding[1 - axis]], self.mesh)
    dtensor_result = math_ops.argmax_v2(
        inputs, axis=axis, output_type=dtypes.int32)
    self.assertDTensorEqual(expect_result, output_layout, dtensor_result)
