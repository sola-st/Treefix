# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/coordinated_read_test.py
cluster = data_service_test_base.TestCluster(num_workers=1)
num_consumers = 3
ds = self.make_coordinated_read_dataset(cluster, num_consumers)
get_next = self.getNext(ds, requires_initialization=True)
_ = [self.evaluate(get_next()) for _ in range(20)]

ds2 = self.make_coordinated_read_dataset(cluster, num_consumers)
with self.assertRaisesRegex(errors.FailedPreconditionError,
                            "current round has already reached"):
    get_next_ds2 = self.getNext(ds2, requires_initialization=True)
    _ = [self.evaluate(get_next_ds2()) for _ in range(20)]
cluster.stop_workers()
