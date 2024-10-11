# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
with ops.device_v2(self.mesh.device_type()):
    seed = constant_op.constant([1, 2])
    expected = gen_stateless_random_ops.stateless_random_uniform_full_int(
        shape=[2, 2], seed=seed, dtype=dtypes.int64)

seed = api.copy_to_mesh(seed, Layout.replicated(rank=1, mesh=self.mesh))
dtensor_result = gen_stateless_random_ops.stateless_random_uniform_full_int(
    shape=[2, 2], seed=seed, dtype=dtypes.int64)
# Note that we only expect the same result (a) for the same device since
# this determines the algorithm, and (b) for fully-replicated output layouts
# since device_id hashing does not reproduce exactly the single-machine
# numbers, only their distribution.
self.assertDTensorEqual(expected, Layout.replicated(rank=2, mesh=self.mesh),
                        dtensor_result)
