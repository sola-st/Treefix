# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils_test.py
truncate_length = 14937  # Experimentally maximum string length loggable.

config = tpu_embedding_configuration_pb2.TPUEmbeddingConfiguration()
for i in range(500):
    td = config.table_descriptor.add()
    td.name = 'table_{}'.format(i)
    td.vocabulary_size = i
config.num_hosts = 2
config.num_tensor_cores = 4
config.batch_size_per_tensor_core = 128

self.assertGreater(
    len(str(config)), truncate_length,
    'Test sanity check: generated config should be of truncating length.')

with self.assertLogs() as logs:
    tpu_embedding_v2_utils.log_tpu_embedding_configuration(config)

self.assertIn('table_499', ''.join(logs.output))
for line in logs.output:
    self.assertLess(
        len(line), truncate_length,
        'Logging function lines should not be of truncating length.')
