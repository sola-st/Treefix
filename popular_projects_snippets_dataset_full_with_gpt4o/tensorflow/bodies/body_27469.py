# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
dataset = dataset_ops.Dataset.list_files(self._filenames,
                                         shuffle=shuffle)
dataset = dataset.flat_map(core_readers.TFRecordDataset)

graph_def = dataset._as_serialized_graph(
    strip_device_assignment=True,
    external_state_policy=options_lib.ExternalStatePolicy.WARN)

options = options_lib.Options()
options.experimental_distribute.auto_shard_policy = sharding_policy

ds1 = distribute._RemoteDataset(graph_def, "/device:CPU:0",
                                dataset.element_spec)
ds2 = distribute._RemoteDataset(graph_def, "/device:CPU:0",
                                dataset.element_spec)

ds1 = ds1.with_options(options)
ds2 = ds2.with_options(options)

ds1 = distribute._AutoShardDataset(ds1, 2, 0)
ds2 = distribute._AutoShardDataset(ds2, 2, 1)

elems1 = set(self.getAllDatasetElements(ds1))
elems2 = set(self.getAllDatasetElements(ds2))

self.assertEmpty(elems1.intersection(elems2))
