# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_bytes_split_op_test.py
expected = ragged_factory_ops.constant_value(expected, dtype=object)
result = ragged_string_ops.string_bytes_split(source)
self.assertAllEqual(expected, result)
