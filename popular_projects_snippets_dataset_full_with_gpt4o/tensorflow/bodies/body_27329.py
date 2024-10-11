# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
num_elements = 100
ds1 = dataset_ops.Dataset.range(num_elements)
ds1 = self.make_distributed_dataset(
    ds1,
    cluster,
    processing_mode="distributed_epoch",
    data_transfer_protocol=self._get_data_transfer_protocol())
ds2 = dataset_ops.Dataset.range(num_elements)
ds2 = self.make_distributed_dataset(
    ds2,
    cluster,
    processing_mode="parallel_epochs",
    data_transfer_protocol=self._get_data_transfer_protocol())
ds = dataset_ops.Dataset.zip((ds1, ds2))
self.assertDatasetProduces(
    ds,
    list(zip(range(num_elements), range(num_elements))),
    assert_items_equal=True)
