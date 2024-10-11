# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/sets_test.py
with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                            "Shape must be a 1D tensor"):
    invalid_shape = 1
    self.evaluate(
        gen_set_ops.set_size(
            set_indices=1,
            set_values=[1, 1],
            set_shape=invalid_shape,
            validate_indices=True,
            name=""))
