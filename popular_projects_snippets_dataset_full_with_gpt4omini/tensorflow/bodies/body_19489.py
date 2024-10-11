# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_optimizer_test.py
def slot_creation_fn(table, slot_names, _):
    slots = {}
    for slot in slot_names:
        slots[slot] = tf_variables.Variable(
            name='{}_{}'.format(table.name, slot),
            initial_value=functools.partial(
                init_ops_v2.Zeros(), shape=table.shape, dtype=dtypes.float32),
            trainable=False)
    exit(slots)
optimizer = tpu_embedding_v2_utils.Adagrad(
    learning_rate=0.1,
    slot_variable_creation_fn=slot_creation_fn)
if use_tpu:
    strategy = self._get_strategy()
else:
    strategy = distribution_strategy_context.get_strategy()
with strategy.scope():
    mid_level = tpu_embedding_v2.TPUEmbedding(
        feature_config=self.feature_config,
        optimizer=optimizer)
    # We aren't going to actually run anything, so the batch_size here does
    # not matter.
    mid_level.build(self.batch_size)
video_accumulator = mid_level._variables['video']['accumulators']
user_accumulator = mid_level._variables['user']['accumulators']
if use_tpu:
    # To check the table contents (ensure that it is zero rather than the
    # normal initial accumulator value specified to in the optimizer config),
    # we need to select the underlying table variable on TPU.
    # We only have one shard on Forge.
    video_accumulator = video_accumulator.variables[0]
    user_accumulator = user_accumulator.variables[0]

self.assertAllClose(video_accumulator.numpy(),
                    np.zeros((self.table_video.vocabulary_size,
                              self.table_video.dim)))
self.assertAllClose(user_accumulator.numpy(),
                    np.zeros((self.table_user.vocabulary_size,
                              self.table_user.dim)))
