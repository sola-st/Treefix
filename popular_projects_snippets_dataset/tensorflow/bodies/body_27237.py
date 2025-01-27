# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/fault_tolerance_test.py
cluster = data_service_test_base.TestCluster(num_workers=1)
num_elements = 100
ds = self.make_distributed_range_dataset(num_elements, cluster)
iterator = iter(ds)
results = []
results.append(next(iterator).numpy())
cluster.stop_dispatcher()
# After the dispatcher dies, the worker should continue providing the rest
# of the dataset's elements.
for _ in range(num_elements - 1):
    results.append(next(iterator).numpy())
self.assertEqual(results, list(range(num_elements)))
