# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/dynamic_sharding_test.py
cluster = data_service_test_base.TestCluster(num_workers=3)
shuffled_filenames = random_ops.random_shuffle(self._filenames)
dataset = dataset_ops.Dataset.from_tensor_slices(shuffled_filenames)
dataset = dataset.interleave(readers.TFRecordDataset)
dataset = self.make_distributed_dataset(
    dataset,
    cluster=cluster,
    processing_mode=data_service_ops.ShardingPolicy.DYNAMIC)
# pylint:disable=g-complex-comprehension
expected = [
    b"Record %d of file %d" % (record, file)
    for file in range(0, 5)
    for record in range(0, 5)
]
self.assertDatasetProduces(
    dataset,
    expected,
    requires_initialization=True,
    assert_items_equal=True)
