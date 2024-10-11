# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/auto_shard_test.py
"""Verifies tf.data service handles every sharding policy with no errors."""
cluster = _make_service_cluster(num_workers=5, local_shard_index=3)
dataset = dataset_ops.Dataset.list_files(self._filenames, shuffle=False)
dataset = dataset.flat_map(readers.TFRecordDataset)
dataset = self.make_distributed_dataset(
    dataset, cluster=cluster, processing_mode=sharding_policy)
self.getDatasetOutput(dataset)
