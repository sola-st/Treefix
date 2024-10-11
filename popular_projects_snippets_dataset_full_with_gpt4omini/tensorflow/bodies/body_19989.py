# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils_test.py
table = tpu_embedding_v2_utils.TableConfig(
    vocabulary_size=2, dim=4,
    combiner='sum', name='table')

self.assertEqual(
    repr(table),
    'TableConfig(vocabulary_size=2, dim=4, initializer=None, '
    'optimizer=None, combiner=\'sum\', name=\'table\', '
    'quantization_config=None)')
