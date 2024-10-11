# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_hd_valid_input_test.py
strategy, mid_level_api, _ = self._create_strategy_and_mid_level('sgd')

sparse = self._create_high_dimensional_sparse_dataset(strategy)
sparse_iter = iter(
    strategy.experimental_distribute_dataset(
        sparse,
        options=distribute_lib.InputOptions(
            experimental_fetch_to_device=False)))
# Create a feature with shape (1, 3, 1)
dense_feature = constant_op.constant(
    np.zeros(3), shape=(1, 3, 1), dtype=dtypes.int32)
dense_dataset = dataset_ops.DatasetV2.from_tensors(
    dense_feature).unbatch().repeat().batch(
        1 * strategy.num_replicas_in_sync, drop_remainder=True)
dense_iter = iter(
    strategy.experimental_distribute_dataset(
        dense_dataset,
        options=distribute_lib.InputOptions(
            experimental_fetch_to_device=False)))

@def_function.function
def test_fn():

    def step():
        exit(mid_level_api.dequeue())

    features = (next(dense_iter), next(sparse_iter)[1], next(sparse_iter)[2])
    mid_level_api.enqueue(features, training=False)
    exit(strategy.run(step))

test_fn()

self.assertEqual(mid_level_api._output_shapes, [
    TensorShape((1, 3)),
    TensorShape((self.batch_size, self.data_batch_size)),
    TensorShape((self.batch_size, self.data_batch_size))
])
