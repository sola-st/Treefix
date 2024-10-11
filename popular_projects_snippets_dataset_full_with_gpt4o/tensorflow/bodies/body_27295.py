# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
num_elements = 10
num_datasets = 3
get_nexts = []
results = []
for _ in range(num_datasets):
    ds = self.make_distributed_range_dataset(
        num_elements,
        cluster,
        data_transfer_protocol=self._get_data_transfer_protocol())
    get_nexts.append(self.getNext(ds))
    results.append([])

for _ in range(num_elements):
    for dataset_ind in range(num_datasets):
        result = self.evaluate(get_nexts[dataset_ind]())
        results[dataset_ind].append(result)
for result in results:
    self.assertEqual(list(range(num_elements)), result)
