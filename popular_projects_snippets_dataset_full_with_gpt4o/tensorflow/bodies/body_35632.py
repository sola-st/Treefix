# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_poisson_test.py
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "overflow"):
    rate = constant_op.constant(1.0, shape=(4, 4, 4, 4, 4))
    self.evaluate(
        random_ops.random_poisson(
            shape=[46902, 51188, 34063, 59195], lam=rate))
