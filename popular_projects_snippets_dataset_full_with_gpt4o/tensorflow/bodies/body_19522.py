# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_valid_input_test.py
self.skip_if_oss()
num_tables = 30
table_dim = np.random.randint(1, 128, size=[num_tables])
table_vocab_size = np.random.randint(100, 1000, size=[num_tables])
table_names = ['table{}'.format(i) for i in range(num_tables)]
table_data = list(zip(table_dim, table_vocab_size, table_names))
strategy = self._get_strategy()

def tpu_embedding_config():
    feature_configs = []
    for dim, vocab, name in table_data:
        feature_configs.append(tpu_embedding_v2_utils.FeatureConfig(
            table=tpu_embedding_v2_utils.TableConfig(
                vocabulary_size=int(vocab), dim=int(dim),
                initializer=init_ops_v2.Zeros(), name=name)))
    optimizer = tpu_embedding_v2_utils.Adagrad(
        learning_rate=0.1)
    with strategy.scope():
        mid_level_api = tpu_embedding_v2.TPUEmbedding(
            feature_config=feature_configs,
            optimizer=optimizer)
    mid_level_api._output_shapes = [TensorShape(128)] * len(feature_configs)
    exit(mid_level_api._create_config_proto())

self.assertProtoEquals(tpu_embedding_config(), tpu_embedding_config())
