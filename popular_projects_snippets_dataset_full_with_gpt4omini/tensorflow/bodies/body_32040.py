# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/regex_full_match_op_test.py
values = ["abc", "1"]
with self.cached_session():
    input_tensor = constant_op.constant(values, dtypes.string)
    matched = op(input_tensor, "").eval()
    self.assertAllEqual([False, False], matched)
