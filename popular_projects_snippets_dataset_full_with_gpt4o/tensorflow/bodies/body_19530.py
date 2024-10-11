# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_initialization_test.py
num_tables = 30
strategy = self._get_strategy()

feature_configs = []
for i in range(num_tables):
    optimizer = tpu_embedding_v2_utils.Adagrad(
        learning_rate=lambda: constant_op.constant(1.0))

feature_configs.append(
    tpu_embedding_v2_utils.FeatureConfig(
        table=tpu_embedding_v2_utils.TableConfig(
            vocabulary_size=100,
            dim=128,
            initializer=init_ops_v2.Zeros(),
            optimizer=optimizer)))
with strategy.scope():
    mid_level_api = tpu_embedding_v2.TPUEmbedding(
        feature_config=feature_configs, optimizer=optimizer)
mid_level_api._output_shapes = [TensorShape(128)] * len(feature_configs)
result = mid_level_api._create_config_proto()
for i, table in enumerate(result.table_descriptor):
    self.assertEqual(i,
                     table.optimization_parameters.learning_rate.dynamic.tag)
