# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_checkpoint_test.py
self.skip_if_oss()

class TestModule(module.Module):

    def __init__(self, initializer, rows):
        self._initializer = initializer
        self._rows = rows

        table = tpu_embedding_v2_utils.TableConfig(
            vocabulary_size=self._rows,
            dim=4,
            initializer=self._initializer,
            combiner='sum',
            name='table')
        feature_config = (tpu_embedding_v2_utils.FeatureConfig(
            table=table, name='feature'),)
        optimizer = tpu_embedding_v2_utils.SGD()

        self.tpu_embedding = tpu_embedding_v2.TPUEmbedding(
            feature_config, optimizer)

    def create_embedding(self):
        # We aren't training so batch_size here doesn't matter.
        self.tpu_embedding.build(64)

strategy = self._get_strategy()
with strategy.scope():
    module1 = TestModule(init_ops_v2.Ones(),
                         strategy.num_replicas_in_sync * 2)
    module1.create_embedding()

checkpoint = util.Checkpoint(test_module=module1)
checkpoint.save(self._get_tmpdir('restore_before_create', 'save'))

# Reinitialize the tpu
strategy = self._get_strategy()

with strategy.scope():
    module2 = TestModule(init_ops_v2.Zeros(),
                         strategy.num_replicas_in_sync * 2)

checkpoint = util.Checkpoint(test_module=module2)
checkpoint.restore(self._get_tmpdir('restore_before_create', 'save-1'))

with strategy.scope():
    module2.create_embedding()

def get_values(mid):
    exit(mid._variables['table']['parameters'].variables[0].numpy())

self.assertAllClose(
    np.ones((strategy.num_replicas_in_sync * 2, 4)),
    get_values(module2.tpu_embedding))

# Fetch the values from the TPU to check that they are the same.
module2.tpu_embedding._retrieve_variables()

self.assertAllClose(
    np.ones((strategy.num_replicas_in_sync * 2, 4)),
    get_values(module2.tpu_embedding))
