# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
test_case.assertEqual(np.int64, np.array(actual.indices).dtype)
test_case.assertAllEqual(expected.indices, actual.indices)

test_case.assertEqual(
    np.array(expected.values).dtype, np.array(actual.values).dtype)
test_case.assertAllEqual(expected.values, actual.values)

test_case.assertEqual(np.int64, np.array(actual.dense_shape).dtype)
test_case.assertAllEqual(expected.dense_shape, actual.dense_shape)
