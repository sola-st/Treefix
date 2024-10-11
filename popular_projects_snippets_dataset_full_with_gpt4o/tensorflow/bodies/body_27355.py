# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(num_workers=1)
num_elements = 10
ds = self.make_distributed_range_dataset(
    num_elements, cluster, compression=compression)
self.assertDatasetProduces(ds, list(range(num_elements)))
