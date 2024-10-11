# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_checkpoint_test.py
# Reinitialize the TPU so that we can re-initialize the embeddings with the
# given optimizer.
if optimizer != tpu_embedding_v2_utils.SGD:
    self.skip_if_oss()
strategy = self._get_strategy()
num_rows = strategy.num_replicas_in_sync

with strategy.scope():
    first_mid_level_contents = np.ones((num_rows, 4))
    first_mid_level_optimizer = optimizer(learning_rate=0.1)
    initializer = init_ops_v2.Constant(first_mid_level_contents)

    table = tpu_embedding_v2_utils.TableConfig(
        vocabulary_size=num_rows,
        dim=4,
        initializer=initializer,
        combiner='sum',
        name='table')
    feature_config = (tpu_embedding_v2_utils.FeatureConfig(
        table=table, name='feature'),)

    first_mid_level = tpu_embedding_v2.TPUEmbedding(
        feature_config, first_mid_level_optimizer)

    first_mid_level.build(64)

cpu_mid_level_optimizer = optimizer(learning_rate=0.1)
cpu_mid_level = tpu_embedding_v2.TPUEmbedding(feature_config,
                                              cpu_mid_level_optimizer)
cpu_mid_level.build(64)

tpu_checkpoint = util.Checkpoint(model=first_mid_level)
tpu_checkpoint.save(self._get_tmpdir('save-tpu', 'save'))
tpu_variables = checkpoint_utils.list_variables(
    self._get_tmpdir('save-tpu'))

cpu_checkpoint = util.Checkpoint(model=cpu_mid_level)
cpu_checkpoint.save(self._get_tmpdir('save-cpu', 'save'))
cpu_variables = checkpoint_utils.list_variables(
    self._get_tmpdir('save-cpu'))

self.assertAllEqual(tpu_variables, cpu_variables)
