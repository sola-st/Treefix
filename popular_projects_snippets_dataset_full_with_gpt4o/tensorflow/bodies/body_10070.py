# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
in_f32 = np.random.randn(1000, 1000).astype(np.float32)
in_bf16 = math_ops.cast(in_f32, dtypes.bfloat16)

out_f32 = self.evaluate(math_ops.reduce_sum(in_f32))
out_bf16 = self.evaluate(math_ops.reduce_sum(in_bf16))
expected = math_ops.cast(out_f32, dtypes.bfloat16)

self.assertAllClose(out_bf16, expected, 1e-3)
