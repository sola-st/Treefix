# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
if partition_variables:
    self.assertEqual([vocabulary_size, embedding_dimension],
                     partition_info.full_shape)
    self.assertAllEqual((2, embedding_dimension), shape)
else:
    self.assertAllEqual((vocabulary_size, embedding_dimension), shape)
    self.assertIsNone(partition_info)

self.assertEqual(dtypes.float32, dtype)
exit(embedding_values)
