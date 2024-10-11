# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_encode_op_test.py
test_flat_values = constant_op.constant([[[72, 101, 108, 108, 111],
                                          [87, 111, 114, 108, 100]],
                                         [[102, 105, 120, 101, 100],
                                          [119, 111, 114, 100, 115]],
                                         [[72, 121, 112, 101, 114],
                                          [99, 117, 98, 101, 46]]])
test_row_splits = [
    constant_op.constant([0, 2, 3], dtype=np.int64),
    constant_op.constant([0, 1, 1, 3], dtype=np.int64)
]
test_value = ragged_tensor.RaggedTensor.from_nested_row_splits(
    test_flat_values, test_row_splits)
expected_value = [[[[u"Hello".encode(encoding), u"World".encode(encoding)]],
                   []],
                  [[[u"fixed".encode(encoding), u"words".encode(encoding)],
                    [u"Hyper".encode(encoding),
                     u"cube.".encode(encoding)]]]]
unicode_encode_op = ragged_string_ops.unicode_encode(test_value, encoding)
self.assertAllEqual(unicode_encode_op, expected_value)
