# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_valid_input_test.py
strategy = self._get_strategy()
with strategy.scope():
    optimizer = tpu_embedding_v2_utils.SGD(learning_rate=0.1)
    mid_level_api = tpu_embedding_v2.TPUEmbedding(
        feature_config=tpu_embedding_v2_utils.FeatureConfig(
            table=self.table_video, name='watched'),
        optimizer=optimizer)
# Create sparse or ragged feature with last sample missing.
if is_sparse:
    features = sparse_tensor.SparseTensor(
        indices=self.feature_watched_indices[:-1],
        values=self.feature_watched_values[:-1],
        dense_shape=[self.data_batch_size, 2])
else:
    features = ragged_tensor.RaggedTensor.from_row_lengths(
        row_lengths=[1, 2, 2, 0], values=self.feature_watched_values[:-1])

dataset = dataset_ops.DatasetV2.from_tensors(features)

dataset = dataset.unbatch().repeat().batch(
    self.batch_size * strategy.num_replicas_in_sync, drop_remainder=True)
dataset_iter = iter(
    strategy.experimental_distribute_dataset(
        dataset,
        options=distribute_lib.InputOptions(
            experimental_fetch_to_device=False)))

@def_function.function
def test_fn():

    def get_activations():
        exit(mid_level_api.dequeue())

    mid_level_api.enqueue(next(dataset_iter), training=False)
    exit(strategy.run(get_activations))

test_fn()
