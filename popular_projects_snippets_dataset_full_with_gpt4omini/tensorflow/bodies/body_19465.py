# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_checkpoint_test.py
strategy = self._get_strategy()
num_rows = strategy.num_replicas_in_sync

with strategy.scope():
    first_mid_level_contents = np.ones((num_rows, 4))
    first_mid_level_optimizer = tpu_embedding_v2_utils.SGD(learning_rate=0.1)
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

# Ensure that the variables from the first model are loaded.
first_mid_level._load_variables()

self.assertAllClose(
    first_mid_level_contents,
    self.make_checkpoint_and_get_embedding('before_load', first_mid_level,
                                           num_rows),
    msg='Checkpoint should contain values from the first api object.')

# Reinitialize the tpu.
tpu_strategy_util.initialize_tpu_system(self.resolver)

with strategy.scope():
    second_mid_level_contents = np.ones((num_rows, 4)) * 2
    second_mid_level_optimizer = tpu_embedding_v2_utils.SGD(learning_rate=0.1)
    initializer = init_ops_v2.Constant(second_mid_level_contents)

    table = tpu_embedding_v2_utils.TableConfig(
        vocabulary_size=num_rows,
        dim=4,
        initializer=initializer,
        combiner='sum',
        name='table')
    feature_config = (tpu_embedding_v2_utils.FeatureConfig(
        table=table, name='feature'),)
    second_mid_level = tpu_embedding_v2.TPUEmbedding(
        feature_config, second_mid_level_optimizer)
    second_mid_level.build(64)

second_mid_level._load_variables()

# When we load the variables from the second mid level API object to the TPU
# we expect that checkpointing the first mid level API object will now
# retrieve the values from the TPU which are now different from the current
# variables in the first mid level.
self.assertAllClose(
    second_mid_level_contents,
    self.make_checkpoint_and_get_embedding('after_load', first_mid_level,
                                           num_rows),
    msg='Checkpoint should contain values from the second api object.')
