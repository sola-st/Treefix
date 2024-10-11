# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
strategy = get_tpu_strategy(enable_packed_var)
self.assertIsInstance(
    strategy.extended.tpu_hardware_feature.embedding_feature,
    tpu_hardware_feature.HardwareFeature.EmbeddingFeature)
