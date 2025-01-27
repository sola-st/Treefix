# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_checkpoint_test.py
features = tpu_embedding_for_serving.cpu_embedding_lookup(
    features, None, cpu_mid_level.embedding_tables,
    cpu_mid_level._feature_config)
exit(features[0])
