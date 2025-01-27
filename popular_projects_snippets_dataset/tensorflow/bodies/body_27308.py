# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
num_elements = 100
num_repetitions = 3
ds1 = self.make_distributed_range_dataset(
    num_elements,
    cluster,
    job_name="job_name",
    data_transfer_protocol=self._get_data_transfer_protocol())
ds1 = ds1.repeat(num_repetitions)
ds2 = self.make_distributed_range_dataset(
    num_elements,
    cluster,
    job_name="job_name",
    data_transfer_protocol=self._get_data_transfer_protocol())
ds2 = ds2.repeat(num_repetitions)
results = []
get_next_1 = self.getNext(ds1)
get_next_2 = self.getNext(ds2)
for _ in range((num_elements * num_repetitions) // 5):
    results.append(self.evaluate(get_next_1()))
for _ in range((num_elements * num_repetitions) // 5):
    results.append(self.evaluate(get_next_2()))
results += self.getIteratorOutput(get_next_1)
results += self.getIteratorOutput(get_next_2)
self.assertCountEqual(num_repetitions * list(range(num_elements)), results)
