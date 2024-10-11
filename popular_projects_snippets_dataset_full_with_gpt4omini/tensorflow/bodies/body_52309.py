# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
test_case.assertEqual(np.int64, np.array(actual.indices).dtype)
test_case.assertAllEqual(expected.indices, actual.indices)

test_case.assertEqual(np.int64, np.array(actual.dense_shape).dtype)
test_case.assertAllEqual(expected.dense_shape, actual.dense_shape)
