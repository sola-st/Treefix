# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/local_workers_test.py
num_local_workers, num_remote_workers = 1, 3
cluster = multi_process_cluster.MultiProcessCluster(
    num_local_workers=num_local_workers,
    num_remote_workers=num_remote_workers)
# Because the elements in datasets are prefetched one per
# CPU core, a static number here may be excessively large
# for small numbers of CPU cores, or too small for high
# CPU core count machines, or probably both.
# In this case the below formula should satisfy both needs.
num_elements = 50 + (multiprocessing.cpu_count() * 2)
num_consumers = 8
iterators = []
for _ in range(num_consumers):
    dataset = self.make_distributed_range_dataset(
        num_elements, cluster, job_name="shared_job")
    iterators.append(self.getNext(dataset))

results = []
for _ in range(10):
    for it in iterators:
        results.append(self.evaluate(it()))
for it in iterators:
    results.extend(self.getIteratorOutput(it))

self.assertCountEqual(results, (num_local_workers + num_remote_workers) *
                      list(range(num_elements)))
