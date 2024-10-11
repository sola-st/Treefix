# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
# This test simulates a distributed environment with 3 workers, each with
# 1 replica.
dataset = dataset_ops.Dataset.range(8)
dataset = dataset.batch(4)
options = options_lib.Options()
options.experimental_distribute.auto_shard_policy = sharding_policy
dataset = dataset.with_options(options)
# We expect the auto-shard rewrite to rewrite RebatchDatasetV2 to
# RebatchDataset(V1) for correctness reasons. This will modify the output
# of the dataset.
worker_a_dataset = dataset.rebatch(batch_size=[2, 1, 1])
if with_prefetch:
    worker_a_dataset = worker_a_dataset.prefetch(1)
worker_a_dataset = distribute._AutoShardDataset(
    worker_a_dataset, 3, 0, num_replicas=3)
expected = [[0, 1], [4, 5]]
self.assertDatasetProduces(worker_a_dataset, expected)

worker_b_dataset = dataset.rebatch(batch_size=[1, 1, 2])
if with_prefetch:
    worker_b_dataset = worker_b_dataset.prefetch(1)
worker_b_dataset = distribute._AutoShardDataset(
    worker_b_dataset, 3, 1, num_replicas=3)
expected = [[2, 3], [6, 7]]
self.assertDatasetProduces(worker_b_dataset, expected)

worker_c_dataset = dataset.rebatch(batch_size=[1, 2, 1])
if with_prefetch:
    worker_c_dataset = worker_c_dataset.prefetch(1)
worker_c_dataset = distribute._AutoShardDataset(
    worker_c_dataset, 3, 2, num_replicas=3)
expected = [[], []]
self.assertDatasetProduces(worker_c_dataset, expected)
