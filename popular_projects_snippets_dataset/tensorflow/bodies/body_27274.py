# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/dynamic_sharding_test.py
num_workers = 3
cluster = data_service_test_base.TestCluster(num_workers)
ds = dataset_ops.Dataset.from_tensor_slices(["a", "b", "c"]).repeat()
ds = ds.enumerate()
ds = self._make_dynamic_sharding_dataset(ds, cluster)
get_next = self.getNext(ds)

counts = collections.defaultdict(int)
while True:
    i, _ = self.evaluate(get_next())
    counts[i] += 1
    # Read until all workers have reached enumeration index 10.
    if counts[10] == num_workers:
        break

for i in range(10):
    self.assertEqual(counts[i], num_workers)
