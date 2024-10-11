# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/cross_trainer_cache_test.py
cluster = self._create_cluster(num_workers=1)
dataset = dataset_ops.Dataset.range(10000000).repeat()
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Cross-trainer caching does not support coordinated reads."):
    dataset = self.make_distributed_dataset(
        dataset,
        cluster,
        job_name="job",
        num_consumers=1,
        consumer_index=0,
        cross_trainer_cache=data_service_ops.CrossTrainerCache(
            trainer_id="Trainer 1"))
    self.getDatasetOutput(dataset)
