# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/coordinated_read_ft_test.py
num_workers = 3
# Set a shutdown quiet period to prevent workers from shutting down partway
# through a round.
cluster = data_service_test_base.TestCluster(
    num_workers, worker_shutdown_quiet_period_ms=2000)
num_consumers = 5
ds = self.make_coordinated_read_dataset(cluster, num_consumers,
                                        sharding_policy)

get_next = self.getNext(ds, requires_initialization=True)
results = []

self.read(get_next, results, 20)
for i in range(num_workers):
    cluster.workers[i].stop()
    self.read(get_next, results, 20)
    cluster.workers[i].restart()
    self.read(get_next, results, 20)

cluster.add_worker()
cluster.restart_dispatcher()
for i in range(num_workers):
    cluster.workers[i].stop()
self.read(get_next, results, 20)

self.checkCoordinatedReadGroups(results, num_consumers)
cluster.stop_workers()
