# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/data_service_ops_test.py
self.skipTest("b/162521601")
sleep_microseconds = int(1e6) * 1000

cluster = data_service_test_base.TestCluster(
    num_workers=1,
    data_transfer_protocol=self._get_data_transfer_protocol())
# Create a dataset which produces the first element quickly, and the second
# element slowly. Fetching the first element triggers prefetching of the
# second element, which we should be able to cancel.
slow = dataset_ops.Dataset.range(1)
slow = slow.apply(testing.sleep(sleep_microseconds))
ds = dataset_ops.Dataset.range(1).concatenate(slow)
ds = self.make_distributed_dataset(
    ds, cluster, data_transfer_protocol=self._get_data_transfer_protocol())
ds = ds.prefetch(1)
get_next = self.getNext(ds)
self.assertEqual(0, self.evaluate(get_next()))
