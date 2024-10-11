# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils_test.py
table = tpu_embedding_v2_utils.TableConfig(
    vocabulary_size=2, dim=4, initializer=None,
    combiner='sum', name='table')

feature_config = tpu_embedding_v2_utils.FeatureConfig(
    table=table, output_shape=[16, 4], name='feature')

self.assertEqual(
    repr(feature_config),
    'FeatureConfig(table=TableConfig(vocabulary_size=2, dim=4, '
    'initializer=None, optimizer=None, combiner=\'sum\', '
    'name=\'table\', quantization_config=None), max_sequence_length=0, '
    'validate_weights_and_indices=True, output_shape=TensorShape([16, 4]), '
    'name=\'feature\')')
