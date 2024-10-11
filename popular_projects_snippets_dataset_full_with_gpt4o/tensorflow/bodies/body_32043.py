# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/regex_full_match_op_test.py
with self.cached_session():
    input_tensor = constant_op.constant("foo", dtypes.string)
    pattern = "[a-z]*"
    op = string_ops.regex_full_match(input_tensor, pattern)
    self.assertTrue(op.name.startswith("StaticRegexFullMatch"), op.name)

    pattern_tensor = constant_op.constant("[a-z]*", dtypes.string)
    op_vec = string_ops.regex_full_match(input_tensor, pattern_tensor)
    self.assertTrue(op_vec.name.startswith("RegexFullMatch"), op.name)
