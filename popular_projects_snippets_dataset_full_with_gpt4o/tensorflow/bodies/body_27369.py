# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/cross_trainer_cache_test.py
cluster = self._create_cluster(num_workers=1)
dataset = dataset_ops.Dataset.range(range_).map(lambda x: x + 1)
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Cross-trainer caching requires the input dataset to be infinite."):
    dataset = dataset.apply(
        data_service_ops.distribute(
            processing_mode=data_service_ops.ShardingPolicy.OFF,
            service=cluster.dispatcher.target,
            job_name="job_name",
            cross_trainer_cache=data_service_ops.CrossTrainerCache(
                trainer_id="Trainer ID")))
    self.getDatasetOutput(dataset)
