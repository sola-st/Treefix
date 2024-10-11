# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/auto_shard_test.py
cluster = _make_service_cluster(num_workers=5, local_shard_index=3)
dataset = dataset_ops.Dataset.list_files(self._filenames, shuffle=False)
dataset = dataset.flat_map(readers.TFRecordDataset)
dataset = self.make_distributed_dataset(
    dataset,
    cluster=cluster,
    processing_mode=data_service_ops.ShardingPolicy.OFF,
    target_workers="LOCAL")

expected = [
    b"Record %d of file %d" % (record, file)
    for file in range(0, 10)
    for record in range(0, 10)
]
self.assertDatasetProduces(dataset, expected)
