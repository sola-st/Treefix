# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_gamma_test.py
# Grappler asserts on size overflow, so this error is only caught when
# running eagerly.
if context.executing_eagerly():
    with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                                "overflow"):
        rate = constant_op.constant(1.0, shape=(4, 4, 4, 4, 4))
        self.evaluate(
            random_ops.random_gamma(
                shape=[46902, 51188, 34063, 59195], alpha=rate))
