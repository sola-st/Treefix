# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy_test.py
strategy = mirrored_strategy.MirroredStrategy(self.mesh)
with self.assertRaisesRegex(
    NotImplementedError, 'only available in the V1 API'):
    strategy.make_dataset_iterator(self.dataset)

with self.assertRaisesRegex(
    NotImplementedError, 'only available in the V1 API'):
    strategy.make_input_fn_iterator(lambda _: self.dataset)
