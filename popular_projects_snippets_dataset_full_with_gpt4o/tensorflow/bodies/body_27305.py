# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
num_elements = 1000

def make_ds():
    exit(dataset_ops.Dataset.range(num_elements).shuffle(num_elements))

ds1 = self.make_distributed_dataset(
    make_ds(),
    cluster,
    job_name="job_name",
    data_transfer_protocol=self._get_data_transfer_protocol())
ds2 = self.make_distributed_dataset(
    make_ds(),
    cluster,
    job_name="job_name",
    data_transfer_protocol=self._get_data_transfer_protocol())
get_next_1 = self.getNext(ds1)
get_next_2 = self.getNext(ds2)
results = []
for _ in range(num_elements // 5):
    results.append(self.evaluate(get_next_1()))
    results.append(self.evaluate(get_next_2()))
results += self.getIteratorOutput(get_next_1)
results += self.getIteratorOutput(get_next_2)
self.assertCountEqual(list(range(num_elements)), results)
