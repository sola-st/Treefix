# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/regex_replace_op_test.py
values = ["abc", "1"]
with self.cached_session():
    input_vector = constant_op.constant(values, dtypes.string)
    stripped = op(input_vector, "", "x")
    self.assertAllEqual([b"xaxbxcx", b"x1x"], stripped)
