# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils_test.py
quantization_config = tpu_embedding_v2_utils.QuantizationConfig(
    num_buckets=10, lower=-1.0, upper=1.0)

self.assertEqual(
    repr(quantization_config),
    'QuantizationConfig(num_buckets=10, lower=-1.0, upper=1.0)')
