# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/fault_tolerance_test.py
cluster = data_service_test_base.TestCluster(num_workers=1)
num_elements_start = 10
num_elements_end = 15
datasets = []
for num_elements in range(num_elements_start, num_elements_end):
    datasets.append(
        self.make_distributed_range_dataset(num_elements, cluster))
    cluster.restart_dispatcher()
for ds, num_elements in zip(datasets,
                            range(num_elements_start, num_elements_end)):
    self.assertDatasetProduces(ds, list(range(num_elements)))
