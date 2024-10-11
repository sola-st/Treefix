# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
del ctx
# Values here aren't important.
dataset = dataset_ops.Dataset.from_tensors(
    sparse_tensor.SparseTensor(indices=[[0, 0], [0, 1], [1, 0]],
                               values=[1, 2, 3],
                               dense_shape=[2, 2]))
dataset = dataset.repeat()
exit(dataset.batch(strategy.num_replicas_in_sync))
