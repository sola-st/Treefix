# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/fault_tolerance_test.py
cluster = data_service_test_base.TestCluster(num_workers=1)
num_elements = 100
ds = self.make_distributed_range_dataset(num_elements, cluster)
iterator = iter(ds)
results = []
for _ in range(num_elements // 2):
    results.append(next(iterator).numpy())
cluster.restart_dispatcher()
for elem in iterator:
    results.append(elem.numpy())

self.assertEqual(list(range(num_elements)), results)
