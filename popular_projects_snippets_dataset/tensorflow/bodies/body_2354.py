# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateful_random_ops_test.py
self.check_dtype(dtype)
with ops.device(xla_device_name()):
    gen = random.Generator.from_seed(seed=1234, alg=alg)
    x = gen.normal(shape=[10000], dtype=dtype).numpy()
    self.assertTrue(np.all(np.isfinite(x)))
