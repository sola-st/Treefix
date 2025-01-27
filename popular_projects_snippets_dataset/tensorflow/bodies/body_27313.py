# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    job_gc_check_interval_ms=50,
    job_gc_timeout_ms=20,
    data_transfer_protocol=self._get_data_transfer_protocol())
num_elements = 10
it1 = iter(
    self.make_distributed_range_dataset(
        num_elements,
        cluster,
        job_name="test1",
        data_transfer_protocol=self._get_data_transfer_protocol()))
it2 = iter(
    self.make_distributed_range_dataset(
        num_elements,
        cluster,
        job_name="test2",
        data_transfer_protocol=self._get_data_transfer_protocol()))
it3 = iter(  # this iterator keeps the task alive. pylint: disable=unused-variable
    self.make_distributed_range_dataset(
        num_elements,
        cluster,
        job_name="test2",
        data_transfer_protocol=self._get_data_transfer_protocol()))
self.assertEqual(cluster.workers[0].num_tasks(), 2)
del it1
del it2
# Check that only the first job is gced. The second job will not be gced
# because there is still an outstanding iterator for it.
while cluster.workers[0].num_tasks() > 1:
    time.sleep(0.1)
self.assertEqual(cluster.workers[0].num_tasks(), 1)
