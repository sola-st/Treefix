# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2_test.py
categorical_column_input = fc_lib.categorical_column_with_identity(
    key='inp', num_buckets=5)
with self.assertRaisesRegex(ValueError, 'tensor_core_shape must be size 2'):
    tpu_fc.shared_embedding_columns_v2([categorical_column_input],
                                       dimension=20,
                                       tensor_core_shape=[None, 20, 15])
