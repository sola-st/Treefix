# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateful_random_ops_test.py
self.check_dtype(dtype)
with ops.device(xla_device_name()):
    gen = random.Generator.from_seed(seed=123, alg=alg)
    n = 100000
    y = gen.truncated_normal(shape=[n], dtype=dtype).numpy()
    random_test_util.test_truncated_normal(
        self.assertEqual, self.assertAllClose, n, y,
        mean_atol=2e-3, median_atol=4e-3,
        variance_rtol=1e-2 if dtype == dtypes.bfloat16 else 5e-3)
