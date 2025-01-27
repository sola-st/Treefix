# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/cross_trainer_cache_test.py
cluster = self._create_cluster(num_workers=1)
dataset = dataset_ops.Dataset.range(10000000).repeat()
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Cross-trainer caching requires named jobs. Got empty `job_name`."):
    dataset = self.make_distributed_dataset(
        dataset,
        cluster,
        job_name=None,
        cross_trainer_cache=data_service_ops.CrossTrainerCache(
            trainer_id="Trainer 1"))
    self.getDatasetOutput(dataset)
