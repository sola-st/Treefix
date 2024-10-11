# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
_assert_sparse_tensor_indices_shape(test_case, expected, actual)

test_case.assertEqual(
    np.array(expected.values).dtype, np.array(actual.values).dtype)
test_case.assertAllEqual(expected.values, actual.values)
