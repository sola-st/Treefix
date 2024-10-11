# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/cross_trainer_cache_test.py
cluster = self._create_cluster(num_workers=2)
dataset = dataset_ops.Dataset.range(10000000).repeat()

with self.assertRaisesRegex(
    ValueError,
    "tf.data service cross-trainer cache requires a non-empty trainer ID."):
    self.make_distributed_dataset(
        dataset,
        cluster,
        job_name="job",
        cross_trainer_cache=data_service_ops.CrossTrainerCache(
            trainer_id=None))
