# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/auto_shard_test.py
cluster = _make_service_cluster(num_workers=5, local_shard_index=3)
dataset = dataset_ops.Dataset.list_files(self._filenames, shuffle=False)
dataset = dataset.interleave(
    readers.TFRecordDataset,
    cycle_length=10,
    num_parallel_calls=dataset_ops.AUTOTUNE)
dataset = dataset.prefetch(buffer_size=dataset_ops.AUTOTUNE)
dataset = self.make_distributed_dataset(
    dataset,
    cluster=cluster,
    processing_mode=data_service_ops.ShardingPolicy.FILE_OR_DATA)
dataset = dataset.prefetch(buffer_size=dataset_ops.AUTOTUNE)

expected = [
    b"Record %d of file %d" % (record, file)
    for record in range(0, 10)
    for file in (3, 8)
]
self.assertDatasetProduces(dataset, expected)
