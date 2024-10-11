# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateful_random_ops_test.py
self.check_dtype(dtype)
minval = 2
maxval = 33
size = 1000
with ops.device(xla_device_name()):
    gen = random.Generator.from_seed(seed=1234, alg=alg)
    x = gen.uniform(
        shape=[size], dtype=dtype, minval=minval, maxval=maxval).numpy()
    self.assertTrue(np.all(x >= minval))
    self.assertTrue(np.all(x <= maxval))
