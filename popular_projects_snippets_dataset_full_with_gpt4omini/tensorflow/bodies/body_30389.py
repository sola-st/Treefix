# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/cast_op_test.py
a = np.random.uniform(-100, 100, 100).astype(np.float32)
with self.cached_session(use_gpu=False):
    b = math_ops.cast(math_ops.cast(a, dtypes.bfloat16), dtypes.float32)
    self.assertAllClose(a, self.evaluate(b), rtol=1 / 128.)
with self.cached_session():
    b = math_ops.cast(math_ops.cast(a, dtypes.bfloat16), dtypes.float32)
    self.assertAllClose(a, self.evaluate(b), rtol=1 / 128.)
