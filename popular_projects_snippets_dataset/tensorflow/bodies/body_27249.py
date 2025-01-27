# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/fault_tolerance_test.py
num_workers = 5
cluster = data_service_test_base.TestCluster(num_workers)
num_elements = 2**55  # Effectively infinite
ds = self.make_distributed_range_dataset(
    num_elements, cluster, max_outstanding_requests=1)
iterator = iter(ds)
zeros_seen = 0
# Read until we've read from all workers. Each worker produces a zero first.
while zeros_seen < num_workers:
    if next(iterator).numpy() == 0:
        zeros_seen += 1

for i in range(num_workers - 1):
    cluster.stop_worker(i)

# Read additional elements to make sure that stopping 4/5 workers doesn't
# result in a hang.
for _ in range(1000):
    next(iterator).numpy()
