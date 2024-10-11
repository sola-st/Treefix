# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/fault_tolerance_test.py
num_workers = 2
cluster = data_service_test_base.TestCluster(num_workers=num_workers)
num_elements = 100
ds = self.make_distributed_range_dataset(num_elements, cluster)
iterator = iter(ds)
results = []

cluster.restart_dispatcher()
for worker_index in range(num_workers):
    cluster.workers[worker_index].restart()
for elem in iterator:
    results.append(elem.numpy())
self.assertCountEqual(num_workers * list(range(num_elements)), results)
cluster.restart_dispatcher()
for worker_index in range(num_workers):
    cluster.workers[worker_index].restart()
for elem in iterator:
    results.append(elem.numpy())
self.assertCountEqual(num_workers * list(range(num_elements)), results)
