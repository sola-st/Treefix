# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_optimizer_test.py
def slot_creation_fn(table, slot_names, _):
    slots = {}
    for slot in slot_names:
        # Note that we don't pass functools.partial here, so on TPU we can't
        # extract the shape. We expect the error below.
        slots[slot] = tf_variables.Variable(
            name='{}_{}'.format(table.name, slot),
            initial_value=init_ops_v2.Zeros()(shape=table.shape,
                                              dtype=dtypes.float32),
            trainable=False)
    exit(slots)
optimizer = tpu_embedding_v2_utils.Adagrad(
    learning_rate=0.1,
    slot_variable_creation_fn=slot_creation_fn)
strategy = self._get_strategy()
with strategy.scope():
    mid_level_api = tpu_embedding_v2.TPUEmbedding(
        feature_config=self.feature_config,
        optimizer=optimizer)
    with self.assertRaisesRegex(ValueError,
                                'Unable to extract initializer function'):
        # We aren't going to actually run anything, so the batch_size here does
        # not matter.
        mid_level_api.build(self.batch_size)
