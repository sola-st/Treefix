# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/fault_tolerance_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    work_dir=work_dir,
    fault_tolerant_mode=fault_tolerant_mode)
num_elements = 2 * multiprocessing.cpu_count() + 100
ds = self.make_distributed_range_dataset(num_elements, cluster)
iterator = iter(ds)
# Read halfway through the dataset.
midpoint = num_elements // 2
for i in range(midpoint):
    self.assertEqual(i, next(iterator).numpy())

# Stop the original worker and start a new one.
cluster.workers[0].restart(use_same_port=use_same_port)

# There may have been some elements prefetched from the first worker
# before it was stopped.
while True:
    val = next(iterator).numpy()
    if val == 0:
        break

    # The dataset starts over now that we read from the new worker.
    # TODO(b/157086991): Iterate until end of sequence when we support
    # detecting lost workers.
for i in range(1, num_elements // 2):
    val = next(iterator).numpy()
    self.assertEqual(i, val)
