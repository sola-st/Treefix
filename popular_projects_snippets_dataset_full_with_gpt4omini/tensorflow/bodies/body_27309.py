# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
dataset = self.make_distributed_range_dataset(
    10,
    cluster,
    job_name="job_name",
    data_transfer_protocol=self._get_data_transfer_protocol())

num_epochs = 5
for _ in range(num_epochs):
    get_next = self.getNext(dataset)
    self.assertEqual(self.getIteratorOutput(get_next), list(range(10)))
