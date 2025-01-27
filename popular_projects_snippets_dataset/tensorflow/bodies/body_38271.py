# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/bincount_op_test.py
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "Shape must be rank 0 but is rank 1"):
    self.evaluate(
        gen_math_ops.ragged_bincount(
            splits=[0, 0, 1],
            values=[1],
            size=[1, 1],
            weights=[0, 0, 0],
            binary_output=False,
            name=None))
