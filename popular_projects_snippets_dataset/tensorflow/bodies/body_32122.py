# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/regex_replace_op_test.py
with self.cached_session():
    input_vector = constant_op.constant("foo", dtypes.string)
    pattern = pattern_fn("[a-z]")
    replace = rewrite_fn(".")
    op = string_ops.regex_replace(input_vector, pattern, replace)
    self.assertTrue(op.name.startswith("RegexReplace"))
