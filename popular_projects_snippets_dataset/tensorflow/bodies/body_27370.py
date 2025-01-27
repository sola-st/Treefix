# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/cross_trainer_cache_test.py
cluster = self._create_cluster(num_workers=1)
dataset = dataset_ops.Dataset.range(10000000).repeat()
dataset1 = self.make_distributed_dataset(
    dataset,
    cluster,
    job_name="job",
    cross_trainer_cache=data_service_ops.CrossTrainerCache(
        trainer_id="Trainer 1"))
# In the eager mode, each iteration creates a new data service job and does
# not reuse cached data. We disallow this use case.
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Cross-trainer caching requires infinite datasets and disallows "
    "multiple repetitions of the same dataset."):
    self.getDatasetOutput(dataset1.take(10))
    self.getDatasetOutput(dataset1.take(10))
    self.getDatasetOutput(dataset1.take(10))
