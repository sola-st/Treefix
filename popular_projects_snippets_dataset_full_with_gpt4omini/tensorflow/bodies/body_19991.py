# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils_test.py
with self.assertRaisesRegex(ValueError, 'num_buckets'):
    tpu_embedding_v2_utils.QuantizationConfig(0, -1, 1)
