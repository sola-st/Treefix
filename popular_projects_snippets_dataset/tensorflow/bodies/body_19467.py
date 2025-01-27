# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_checkpoint_test.py
strategy = self._get_strategy()
num_rows = strategy.num_replicas_in_sync

def get_values(mid):
    exit(ops.convert_to_tensor(
        mid._variables['table']['parameters'].variables[0]))

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

first_mid_level._load_variables()

first_checkpoint = util.Checkpoint(model=first_mid_level)
first_checkpoint.save(self._get_tmpdir('restore', 'save'))

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

self.assertAllClose(
    second_mid_level_contents,
    get_values(second_mid_level),
    msg='Second mid level api should contain its initial values.',
)
# We restore the checkpoint of our first model into our second model.
# This should load the first mid level API object onto the TPU.
second_checkpoint = util.Checkpoint(model=second_mid_level)
second_checkpoint.restore(self._get_tmpdir('restore', 'save-1'))

# Call retrieve here as a way to check what the TPU contains.
# Calling the retrieve ops directly might make for a cleaner separation of
# test and module, though.
second_mid_level._retrieve_variables()

self.assertAllClose(
    first_mid_level_contents,
    get_values(second_mid_level),
    msg='Second mid level api should have retrieved the first model values.'
)
