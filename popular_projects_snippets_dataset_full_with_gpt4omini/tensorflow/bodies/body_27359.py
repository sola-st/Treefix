# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/cross_trainer_cache_test.py
# Fetching an element from the dataset will trigger prefetches of more
# elements, one per CPU core which will be placed in the cache.
# However if the number of prefetches exceeds the space available in
# the cache then the sliding window will be moved forward away from
# the element just read thus negating the use of the cache as other
# trainers will not get the correct element.
# Hence the need to calculate the size of the cache based on the
# number of CPU cores and the element size of 423. The extra 8
# entries are simply a bit of margin.
num_cpus = multiprocessing.cpu_count()
cluster = self._create_cluster(
    num_workers=1, cross_trainer_cache_size_bytes=(num_cpus + 8) * 423)
num_readers = 20
num_elements = 50
dataset = dataset_ops.Dataset.range(10000000).repeat()

datasets = []
iterators = []
for i in range(num_readers):
    distributed_dataset = self.make_distributed_dataset(
        dataset,
        cluster,
        job_name="job",
        cross_trainer_cache=data_service_ops.CrossTrainerCache(
            trainer_id=f"Trainer {i}"),
        max_outstanding_requests=1)
    iterator = self.getNext(distributed_dataset)
    datasets.append(distributed_dataset)
    iterators.append(iterator)

for i in range(num_elements):
    # All the readers read the same element in one step.
    for j in range(num_readers):
        self.assertEqual(self.evaluate(iterators[j]()), i)
