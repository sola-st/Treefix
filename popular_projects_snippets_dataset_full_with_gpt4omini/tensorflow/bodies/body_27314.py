# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=3,
    job_gc_check_interval_ms=50,
    job_gc_timeout_ms=20,
    data_transfer_protocol=self._get_data_transfer_protocol())
num_elements = 1000
# Repeatedly create and garbage-collect the same job.
for _ in range(3):
    ds = self.make_distributed_range_dataset(
        num_elements,
        cluster,
        job_name="test",
        data_transfer_protocol=self._get_data_transfer_protocol())
    it = iter(ds)
    for _ in range(50):
        next(it)
    del it
    # Wait for the task to be garbage-collected on all workers.
    while cluster.num_tasks_on_workers() > 0:
        time.sleep(0.1)
