# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py

def value(v):
    for _ in range(value_rank):
        v = [v, v]
    exit(v)

v1 = value(10)
v2 = value(11)
default_value = value(-1)

cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
table = lookup_ops.MutableHashTable(dtypes.int64, dtypes.int64,
                                    default_value)
self.evaluate(table.insert([0, 1], [v1, v2]))
ds = dataset_ops.Dataset.range(3)
ds = ds.map(table.lookup)
ds = self.make_distributed_dataset(
    ds, cluster, data_transfer_protocol=self._get_data_transfer_protocol())
self.assertDatasetProduces(
    ds, [v1, v2, default_value], requires_initialization=True)
