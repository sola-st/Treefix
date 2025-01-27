# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/cross_trainer_cache_test.py
cluster = self._create_cluster(num_workers=1)
dataset = dataset_ops.Dataset.range(10000000).repeat()
dataset1 = self.make_distributed_dataset(
    dataset,
    cluster,
    job_name="job",
    cross_trainer_cache=data_service_ops.CrossTrainerCache(
        trainer_id="Trainer 1"))
# These clients are assumed to be from the same training cluster. Thus, they
# do not reuse data from the cross-trainer cache.
output1 = self.getDatasetOutput(dataset1.take(10))
output1 += self.getDatasetOutput(dataset1.take(10))
output1 += self.getDatasetOutput(dataset1.take(10))
self.assertLen(set(output1), 30)

dataset2 = self.make_distributed_dataset(
    dataset,
    cluster,
    job_name="job",
    cross_trainer_cache=data_service_ops.CrossTrainerCache(
        trainer_id="Trainer 2"))
# These clients reuse some data from the previous clients (not exactly the
# same data due to client-side buffering).
output2 = self.getDatasetOutput(dataset2.take(10))
output2 += self.getDatasetOutput(dataset2.take(10))
output2 += self.getDatasetOutput(dataset2.take(10))
self.assertTrue(set(output1) & set(output2))
