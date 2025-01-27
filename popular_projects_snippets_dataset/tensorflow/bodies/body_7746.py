# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
strategy = get_tpu_strategy()
def dataset_fn(ctx):
    del ctx
    # Values here aren't important.
    dataset = dataset_ops.Dataset.from_tensors(
        ragged_tensor.RaggedTensor.from_row_splits(
            values=[1, 2, 3],
            row_splits=[0, 2, 3]))
    dataset = dataset.repeat()
    exit(dataset.batch(strategy.num_replicas_in_sync))

with self.assertRaisesRegex(ValueError, "TPUStrategy does not support"):
    iter(strategy.distribute_datasets_from_function(dataset_fn))
