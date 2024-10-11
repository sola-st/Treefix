# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/regex_replace_op_test.py
values = ["a:foo", "a:bar", "a:foo", "b:baz", "b:qux", "ca:b"]
with self.cached_session():
    input_vector = constant_op.constant(values, dtypes.string)
    stripped = op(input_vector, "^(a:|b:)", "", replace_global=False)
    self.assertAllEqual([b"foo", b"bar", b"foo", b"baz", b"qux", b"ca:b"],
                        stripped)
