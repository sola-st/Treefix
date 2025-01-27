# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
"""Test calling operations with benign NaN output."""
check_numerics_callback.enable_check_numerics()

# Empty input tensor
x = constant_op.constant(1, dtype=dtypes.float32, shape=[0, 1, 1, 1])
scale = constant_op.constant([1], dtype=dtypes.float32)
offset = constant_op.constant([1], dtype=dtypes.float32)

# Calling fused_batch_norm with an empty input should output a NaN in the
# latter four outputs without triggering the check_numerics callback
batch_norm_res = gen_nn_ops._fused_batch_norm(
    x=x, scale=scale, offset=offset, mean=[], variance=[])

_, batch_mean, batch_variance, _, _ = self.evaluate(batch_norm_res)

self.assertTrue(np.isnan(batch_mean.squeeze()))
self.assertTrue(np.isnan(batch_variance.squeeze()))
