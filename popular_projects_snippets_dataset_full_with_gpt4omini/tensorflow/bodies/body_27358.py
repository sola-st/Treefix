# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/cross_trainer_cache_test.py
cluster = self._create_cluster(num_workers=1)
dataset = dataset_ops.Dataset.range(10000000).repeat()
dataset1 = self.make_distributed_dataset(dataset, cluster, job_name="job")
self.assertDatasetProduces(dataset1.take(10), list(range(10)))

# The two clients use the same job. The second client can't read the data
# already read by the first client.
dataset2 = self.make_distributed_dataset(dataset, cluster, job_name="job")
output = self.getDatasetOutput(dataset2.take(10))
self.assertGreaterEqual(output[0], 10)
