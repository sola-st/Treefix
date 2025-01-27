# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v1_checkpoint_test.py
strategy = self._get_strategy()
with strategy.scope():
    first_mid_level_contents = np.ones((4, 4))
    first_mid_level_optimizer = tpu_embedding_v2_utils.SGD(learning_rate=0.1)
    initializer = init_ops_v2.Constant(first_mid_level_contents)

    table = tpu_embedding_v2_utils.TableConfig(
        vocabulary_size=4,
        dim=4,
        initializer=initializer,
        combiner='sum',
        name='table')
    feature_config = (tpu_embedding_v2_utils.FeatureConfig(
        table=table, name='feature'),)

    first_mid_level = tpu_embedding_v1.TPUEmbeddingV0(
        feature_config, first_mid_level_optimizer)
    first_mid_level.build()

first_checkpoint = util.Checkpoint(model=first_mid_level)
first_checkpoint.save(self._get_tmpdir('restore', 'save'))

with strategy.scope():
    second_mid_level_contents = np.ones((4, 4)) * 2
    second_mid_level_optimizer = tpu_embedding_v2_utils.SGD(learning_rate=0.1)
    initializer = init_ops_v2.Constant(second_mid_level_contents)

    table = tpu_embedding_v2_utils.TableConfig(
        vocabulary_size=4,
        dim=4,
        initializer=initializer,
        combiner='sum',
        name='table')
    feature_config = (tpu_embedding_v2_utils.FeatureConfig(
        table=table, name='feature'),)
    second_mid_level = tpu_embedding_v1.TPUEmbeddingV0(
        feature_config, second_mid_level_optimizer)
    second_mid_level.build()
# We restore the checkpoint of our first model into our second model.
second_checkpoint = util.Checkpoint(model=second_mid_level)
second_checkpoint.restore(self._get_tmpdir('restore', 'save-1'))

self.assertAllClose(
    first_mid_level_contents,
    second_mid_level._variables['table']['parameters'].numpy(),
    msg='Second mid level api should have restored the first model values.')
