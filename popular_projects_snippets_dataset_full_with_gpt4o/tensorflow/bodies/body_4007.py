# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
x = stateless_random_ops.stateless_random_uniform(
    shape=[4, 8], seed=[0, 1], dtype=dtypes.float32
)
y = constant_op.constant(7, dtype=dtypes.float32)

expected_result = math_ops.Mod(x=x, y=y)
expected_layout = Layout.replicated(self.mesh, rank=2)
dtensor_result = math_ops.Mod(
    x=numpy_util.pack_numpy(x, layout=Layout(shard_specs, self.mesh)),
    y=numpy_util.pack_numpy(y, layout=Layout([], self.mesh)),
)

self.assertDTensorEqual(expected_result, expected_layout, dtensor_result)
