# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/regex_full_match_op_test.py
values = ["abc", "1"]
with self.cached_session():
    input_tensor = constant_op.constant(values, dtypes.string)
    invalid_pattern = "A["
    matched = op(input_tensor, invalid_pattern)
    with self.assertRaisesOpError("Invalid pattern"):
        self.evaluate(matched)
