# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/coordinated_read_ft_test.py
starting_workers = 3
cluster = data_service_test_base.TestCluster(num_workers=starting_workers)
num_consumers = 7
ds = self.make_coordinated_read_dataset(cluster, num_consumers)

get_next = self.getNext(ds, requires_initialization=True)
results = []
zeros_seen = 0
for _ in range(25):
    results.append(self.evaluate(get_next()))
    if results[-1] == 0:
        zeros_seen += 1
for _ in range(workers_to_add):
    cluster.add_worker()
# Read until all new workers have joined.
while zeros_seen < starting_workers + workers_to_add:
    results.append(self.evaluate(get_next()))
    if results[-1] == 0:
        zeros_seen += 1
    # Read some more.
for _ in range(25):
    results.append(self.evaluate(get_next()))

self.checkCoordinatedReadGroups(results, num_consumers)
cluster.stop_workers()
