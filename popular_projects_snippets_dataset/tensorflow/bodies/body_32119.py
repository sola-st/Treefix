# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/regex_replace_op_test.py
values = ["ababababab", "abcabcabc", ""]
with self.cached_session():
    input_vector = constant_op.constant(values, dtypes.string)
    stripped = op(input_vector, "ab", "abc", True)
    self.assertAllEqual([b"abcabcabcabcabc", b"abccabccabcc", b""], stripped)
