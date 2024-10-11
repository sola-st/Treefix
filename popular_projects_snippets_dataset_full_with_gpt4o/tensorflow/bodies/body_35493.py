# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_binomial_test.py
rnd = stateful_random_ops.Generator.from_seed(12345).binomial([0], [], [])
self.assertEqual([0], rnd.shape.as_list())
