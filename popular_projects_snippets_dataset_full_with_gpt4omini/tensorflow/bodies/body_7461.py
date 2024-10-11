# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy_test.py
elements = [[1, 2, 3], [1, 2], [1, 2, 3, 4]]
dataset = dataset_ops.Dataset.from_generator(
    lambda: elements, dtypes.int64).repeat()
strategy = mirrored_strategy.MirroredStrategy(self.mesh)
with self.assertRaisesRegex(ValueError, 'requires a static batch size'):
    strategy.experimental_distribute_dataset(dataset)
