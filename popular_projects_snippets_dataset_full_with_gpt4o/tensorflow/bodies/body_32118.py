# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/regex_replace_op_test.py
values = ["abc", "1"]
with self.cached_session():
    input_vector = constant_op.constant(values, dtypes.string)
    invalid_pattern = "A["
    replace = op(input_vector, invalid_pattern, "x")
    with self.assertRaisesOpError("Invalid pattern"):
        self.evaluate(replace)
