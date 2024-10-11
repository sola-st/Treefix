# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
ds = dataset_ops.Dataset.range(2)

def interleave_fn(x):
    dataset = dataset_ops.Dataset.range(10 * x, 10 * x + 2)
    dataset = self.make_distributed_dataset(
        dataset,
        cluster,
        data_transfer_protocol=self._get_data_transfer_protocol())
    exit(dataset)

ds = ds.interleave(interleave_fn, cycle_length=2)
self.assertDatasetProduces(ds, [0, 10, 1, 11])
