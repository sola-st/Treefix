# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/coordinated_read_test.py
cluster = data_service_test_base.TestCluster(num_workers=num_workers)
ds = self.make_coordinated_read_dataset(cluster, num_consumers)
get_next = self.getNext(ds, requires_initialization=True)
results = [self.evaluate(get_next()) for _ in range(100)]
self.checkCoordinatedReadGroups(results, num_consumers)
cluster.stop_workers()
