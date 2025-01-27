# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/auto_shard_test.py
cluster = multi_process_cluster.MultiProcessCluster(
    num_local_workers=0, num_remote_workers=3)
dataset = dataset_ops.Dataset.list_files(self._filenames, shuffle=False)
dataset = dataset.flat_map(readers.TFRecordDataset)
dataset = self.make_distributed_dataset(
    dataset,
    cluster=cluster,
    processing_mode=data_service_ops.ShardingPolicy.FILE_OR_DATA)
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Static sharding policy <FILE_OR_DATA> requires local tf.data workers"):
    self.getDatasetOutput(dataset)
