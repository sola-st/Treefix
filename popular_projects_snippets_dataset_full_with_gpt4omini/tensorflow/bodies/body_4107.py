# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
src_numpy = np.random.uniform(size=src_shape)
src = constant_op.constant(src_numpy, dtype=dtypes.float32)

expected = gen_array_ops.tile(src, multiples)

src = numpy_util.pack_numpy(src,
                            self.layouts[src_sharding_dim][len(src_shape)])
with api._dtensor_device()._default_layout(
    self.layouts[target_sharding_dim][len(src_shape)]):
    dtensor_result = gen_array_ops.tile(src, multiples)
self.assertDTensorEqual(expected,
                        self.layouts[target_sharding_dim][len(src_shape)],
                        dtensor_result)
