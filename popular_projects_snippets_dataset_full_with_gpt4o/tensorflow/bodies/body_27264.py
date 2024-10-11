# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/dynamic_sharding_test.py
num_workers = 5
cluster = data_service_test_base.TestCluster(num_workers=num_workers)
# Less than the number of workers, so that some workers get zero elements on
# the first repetition.
num_elements = 1
ds = dataset_ops.Dataset.range(num_elements).repeat()
ds = self._make_dynamic_sharding_dataset(ds, cluster)
get_next = self.getNext(ds)
for _ in range(20):
    self.assertEqual(self.evaluate(get_next()), 0)

# Stop all but one worker and check that we can still read.
for i in range(num_workers - 1):
    cluster.workers[i].stop()
for _ in range(20):
    self.assertEqual(self.evaluate(get_next()), 0)
