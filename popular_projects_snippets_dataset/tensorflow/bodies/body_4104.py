# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
src_numpy = np.random.uniform(size=src_shape)
src = constant_op.constant(src_numpy, dtype=dtypes.float32)

expected = array_ops.reshape(src, target_shape)

src = numpy_util.pack_numpy(src,
                            self.layouts[src_sharding_dim][len(src_shape)])
dtensor_result = array_ops.reshape(src, target_shape)
self.assertDTensorEqual(
    expected, self.layouts[target_sharding_dim][len(target_shape)],
    dtensor_result)
