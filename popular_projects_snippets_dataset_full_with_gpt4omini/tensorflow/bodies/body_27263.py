# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/dynamic_sharding_test.py
cluster = data_service_test_base.TestCluster(num_workers=2)
num_elements = 20
elements_to_read = 1000
ds = dataset_ops.Dataset.range(num_elements).repeat()
ds = self._make_dynamic_sharding_dataset(ds, cluster)
get_next = self.getNext(ds)
results = {}
for _ in range(elements_to_read):
    val = self.evaluate(get_next())
    if val not in results:
        results[val] = 0
    results[val] += 1
for i in range(num_elements):
    self.assertGreater(results[i], elements_to_read / num_elements / 2)
