# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/fault_tolerance_test.py
cluster = data_service_test_base.TestCluster(num_workers=1)
num_elements = 100
ds = self.make_distributed_range_dataset(num_elements, cluster)

cluster.restart_dispatcher()
cluster.workers[0].restart()
self.assertDatasetProduces(ds, list(range(num_elements)))
cluster.restart_dispatcher()
cluster.workers[0].restart()
self.assertDatasetProduces(ds, list(range(num_elements)))
