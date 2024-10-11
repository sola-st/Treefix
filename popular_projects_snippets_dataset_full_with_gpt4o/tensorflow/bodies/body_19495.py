# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_hd_valid_input_test.py
strategy, mid_level_api, _ = self._create_strategy_and_mid_level('sgd')

dataset = self._create_high_dimensional_dense_dataset(strategy)
dense_iter = iter(
    strategy.experimental_distribute_dataset(
        dataset,
        options=distribute_lib.InputOptions(
            experimental_fetch_to_device=False)))

sparse = self._create_high_dimensional_sparse_dataset(strategy)
sparse_iter = iter(
    strategy.experimental_distribute_dataset(
        sparse,
        options=distribute_lib.InputOptions(
            experimental_fetch_to_device=False)))

ragged = self._create_high_dimensional_ragged_dataset(strategy)
ragged_iter = iter(
    strategy.experimental_distribute_dataset(
        ragged,
        options=distribute_lib.InputOptions(
            experimental_fetch_to_device=False)))

mid_level_api.build([
    TensorShape([self.batch_size, self.data_batch_size, 1]),
    TensorShape([self.batch_size, self.data_batch_size, 2]),
    TensorShape([self.batch_size, self.data_batch_size, 3])
])

@def_function.function
def test_fn():

    def step():
        exit(mid_level_api.dequeue())

    features = (next(dense_iter)[0], next(sparse_iter)[1],
                next(ragged_iter)[2])
    mid_level_api.enqueue(features, training=False)
    exit(strategy.run(step))

test_fn()
