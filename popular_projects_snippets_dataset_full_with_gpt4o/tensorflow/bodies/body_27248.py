# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/fault_tolerance_test.py
cluster = data_service_test_base.TestCluster(num_workers=1)
num_elements = 2 * multiprocessing.cpu_count() + 100
ds = self.make_distributed_range_dataset(num_elements, cluster)
iterator = iter(ds)
results = []
# Read halfway through the dataset.
for _ in range(num_elements // 2):
    results.append(next(iterator).numpy())

cluster.add_worker()
# Wait for the new worker to register with the dispatcher.
while cluster.num_registered_workers() < 2:
    time.sleep(10 / 1000)  # 10ms

for elem in iterator:
    results.append(elem.numpy())

self.assertCountEqual(2 * list(range(num_elements)), results)
