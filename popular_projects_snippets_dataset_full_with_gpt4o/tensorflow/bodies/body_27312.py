# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    job_gc_check_interval_ms=50,
    job_gc_timeout_ms=20,
    data_transfer_protocol=self._get_data_transfer_protocol())
num_elements = 100
ds = self.make_distributed_range_dataset(
    num_elements,
    cluster,
    job_name=job_name,
    data_transfer_protocol=self._get_data_transfer_protocol())
it = iter(ds)
self.assertEqual(next(it).numpy(), 0)
self.assertEqual(cluster.workers[0].num_tasks(), 1)
del it
while cluster.workers[0].num_tasks() > 0:
    time.sleep(0.1)
