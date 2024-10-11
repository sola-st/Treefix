# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
inputs = constant_op.constant([1, 2, 3])
shape = [3, 3]
expected = gen_array_ops.broadcast_to(inputs, shape)

inputs = api.copy_to_mesh(inputs, Layout.replicated(self.mesh, rank=1))
with api.run_on(self.mesh):
    dtensor_result = gen_array_ops.broadcast_to(inputs, shape)

self.assertDTensorEqual(expected, Layout.replicated(self.mesh, rank=2),
                        dtensor_result)
