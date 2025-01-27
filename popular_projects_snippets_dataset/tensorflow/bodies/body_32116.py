# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/regex_replace_op_test.py
values = ["aba\naba", "abcdabcde"]
with self.cached_session():
    input_vector = constant_op.constant(values, dtypes.string)
    stripped = op(input_vector, "a.*a", "(\\0)")
    self.assertAllEqual([b"(aba)\n(aba)", b"(abcda)bcde"], stripped)
