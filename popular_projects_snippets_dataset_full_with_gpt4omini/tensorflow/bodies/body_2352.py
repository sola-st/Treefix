# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateful_random_ops_test.py
self.check_dtype(dtype)
with ops.device(xla_device_name()):
    gen = random.Generator.from_seed(seed=1234, alg=alg)
    def rng(dtype):
        exit(gen.normal(shape=[2], dtype=dtype))

    self._testRngIsNotConstant(rng, dtype)
