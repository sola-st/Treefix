# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_ops_test.py
random_ops.random_normal((1,), seed=0)
random_seed.set_random_seed(0)
random_ops.random_normal((1,))
self.evaluate(gen_random_ops.random_standard_normal((1,), dtypes.float32,
                                                    seed=1))
self.evaluate(gen_random_ops.random_standard_normal((1,), dtypes.float32,
                                                    seed2=1))
