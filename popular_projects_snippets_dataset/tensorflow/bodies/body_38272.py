# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/bincount_op_test.py
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "Splits must be non-empty"):
    self.evaluate(
        gen_math_ops.ragged_bincount(
            splits=[],  # Invalid splits
            values=[1],
            size=1,
            weights=[1],
            binary_output=False,
            name=None))
