# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/cross_trainer_cache_test.py
cluster = self._create_cluster(
    num_workers=1, cross_trainer_cache_size_bytes=500)
dataset = dataset_ops.Dataset.range(10000000).repeat()
num_readers = 20

for i in range(num_readers):
    # Even if the cache is small and may discard old data, each trainer can
    # still read the required number of elements because the input dataset is
    # infinite.
    distributed_dataset = self.make_distributed_dataset(
        dataset,
        cluster,
        job_name="job",
        cross_trainer_cache=data_service_ops.CrossTrainerCache(
            trainer_id=f"Trainer {i}"))
    output = self.getDatasetOutput(distributed_dataset.take(200))
    self.assertLen(output, 200)
