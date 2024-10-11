# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/string_split_op_test.py
if error is not None:
    with self.assertRaisesRegex(ValueError, error):
        ragged_string_ops.string_split(source, sep, skip_empty, delimiter,
                                       result_type)
if expected is not None:
    result = ragged_string_ops.string_split(source, sep, skip_empty,
                                            delimiter, result_type)
    if isinstance(expected, sparse_tensor.SparseTensorValue):
        self.assertAllEqual(result.indices, expected.indices)
        self.assertAllEqual(result.values, expected.values)
        self.assertAllEqual(result.dense_shape, expected.dense_shape)
    else:
        self.assertAllEqual(result, expected)
