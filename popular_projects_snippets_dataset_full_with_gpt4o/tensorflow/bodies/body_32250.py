# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_script_op_test.py
inputs = [-100, 0xffffff]
with self.cached_session():
    input_vector = constant_op.constant(inputs, dtypes.int32)
    outputs = string_ops.unicode_script(input_vector).eval()
    self.assertAllEqual(outputs, [-1, -1])
