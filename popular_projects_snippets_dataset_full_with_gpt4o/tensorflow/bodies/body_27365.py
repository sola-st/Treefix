# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/cross_trainer_cache_test.py
cluster = self._create_cluster(num_workers=2)
dataset = dataset_ops.Dataset.range(10000000).repeat()
dataset1 = self.make_distributed_dataset(
    dataset,
    cluster,
    processing_mode=data_service_ops.ShardingPolicy.DYNAMIC,
    job_name="job",
    cross_trainer_cache=data_service_ops.CrossTrainerCache(
        trainer_id="Trainer 1"))
output1 = self.getDatasetOutput(dataset1.take(100))

# The second client reads the same data from the cross-trainer cache.
dataset2 = self.make_distributed_dataset(
    dataset,
    cluster,
    processing_mode=data_service_ops.ShardingPolicy.DYNAMIC,
    job_name="job",
    cross_trainer_cache=data_service_ops.CrossTrainerCache(
        trainer_id="Trainer 2"))
output2 = self.getDatasetOutput(dataset2.take(100))
# Verifies the intersection is non-empty.
self.assertTrue(set(output1) & set(output2))
