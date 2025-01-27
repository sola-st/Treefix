# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/coordinated_read_ft_test.py
num_workers = 3
# Set a shutdown quiet period to prevent workers from shutting down partway
# through a round.
cluster = data_service_test_base.TestCluster(
    num_workers, worker_shutdown_quiet_period_ms=2000)
num_consumers = 5
ds = self.make_coordinated_read_dataset(cluster, num_consumers)

get_next = self.getNext(ds, requires_initialization=True)
results = []

self.read(get_next, results, 20)
cluster.workers[1].stop()
# Check that we can continue to read even with a worker stopped.
self.read(get_next, results, 20)
cluster.workers[1].restart()
# Read until we get results from the restarted worker, then read some more.
while results[-1] != 0:
    results.append(self.evaluate(get_next()))
self.read(get_next, results, 20)
self.checkCoordinatedReadGroups(results, num_consumers)
cluster.stop_workers()
