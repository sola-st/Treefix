# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/regex_full_match_op_test.py
values = ["abaaba", "abcdabcde"]
with self.cached_session():
    input_tensor = constant_op.constant(values, dtypes.string)
    matched = op(input_tensor, "a.*a").eval()
    self.assertAllEqual([True, False], matched)
