# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
inputs = constant_op.constant([[1, 2, 3, 4], [5, 6, 7, 8]],
                              dtype=dtypes.float32)

with backprop.GradientTape() as tape:
    tape.watch([inputs])
    expected_result = gen_math_ops.tanh(inputs)
expected_grad = tape.gradient(expected_result, [inputs])

layout = Layout(sharding, self.mesh)
inputs = numpy_util.pack_numpy(inputs.numpy(), layout)
with api.run_on(self.mesh):
    with backprop.GradientTape() as tape:
        tape.watch([inputs])
        dtensor_result = gen_math_ops.tanh(inputs)
    dtensor_grad = tape.gradient(dtensor_result, [inputs])
# df2x2 lowers the tanh preceision to 1e-4.
self.assertDTensorEqual(
    expected_grad[0],
    layout,
    dtensor_grad[0],
    tol=1e-4
    if 'TPU' in self.mesh.local_devices()[0] else test_util.DEFAULT_TOL)
