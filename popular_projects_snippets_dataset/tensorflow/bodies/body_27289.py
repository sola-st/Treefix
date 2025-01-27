# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
initializer = self.lookupTableInitializer(init_source, [10, 11])
table = lookup_ops.StaticHashTable(initializer, -1)
ds = dataset_ops.Dataset.range(3)
ds = ds.map(table.lookup)
ds = self.make_distributed_dataset(
    ds, cluster, data_transfer_protocol=self._get_data_transfer_protocol())
self.evaluate(lookup_ops.tables_initializer())
self.assertDatasetProduces(ds, [10, 11, -1], requires_initialization=True)
