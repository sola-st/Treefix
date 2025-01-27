# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_split_op_test.py
with self.assertRaisesRegex(ValueError, "result_type must be .*"):
    ragged_string_ops.strings_split_v1("foo", result_type="BouncyTensor")
