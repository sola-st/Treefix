# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_hd_invalid_input_test.py
strategy, mid_level_api, _ = self._create_strategy_and_mid_level('sgd')

sparse = self._create_high_dimensional_sparse_dataset(strategy)
sparse_iter = iter(
    strategy.experimental_distribute_dataset(
        sparse,
        options=distribute_lib.InputOptions(
            experimental_fetch_to_device=False)))

mid_level_api._output_shapes = [TensorShape((1, 1)) for _ in range(3)]
# The output shape passed to build method is consistent.
mid_level_api.build([TensorShape([1, 1, 1]) for _ in range(3)])

@def_function.function
def test_fn():

    def step():
        exit(mid_level_api.dequeue())

    mid_level_api.enqueue(next(sparse_iter), training=False)
    exit(strategy.run(step))

# Enqueued tensor has shape inconsistent with the output shape setting.
with self.assertRaisesRegex(ValueError,
                            'Inconsistent shape founded for input feature'):
    test_fn()
