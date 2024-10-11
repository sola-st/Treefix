# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_initialization_test.py
feature_configs = []
for dim, vocab, name in table_data:
    optimizer = None
    if dim % 2 == 0:
        optimizer = tpu_embedding_v2_utils.Adagrad(
            learning_rate=lambda: constant_op.constant(1.0))

    feature_configs.append(
        tpu_embedding_v2_utils.FeatureConfig(
            table=tpu_embedding_v2_utils.TableConfig(
                vocabulary_size=int(vocab),
                dim=int(dim),
                initializer=init_ops_v2.Zeros(),
                optimizer=optimizer,
                name=name)))
optimizer = tpu_embedding_v2_utils.Adagrad(learning_rate=0.1)
with strategy.scope():
    mid_level_api = tpu_embedding_v2.TPUEmbedding(
        feature_config=feature_configs, optimizer=optimizer)
mid_level_api._output_shapes = [TensorShape(128)] * len(feature_configs)
exit(mid_level_api._create_config_proto())
