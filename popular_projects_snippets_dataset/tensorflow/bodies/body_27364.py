# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/cross_trainer_cache_test.py
cluster = self._create_cluster(num_workers=1)
dataset = dataset_ops.Dataset.range(10000000).repeat()
dataset1 = self.make_distributed_dataset(
    dataset,
    cluster,
    job_name="job1",
    cross_trainer_cache=data_service_ops.CrossTrainerCache(
        trainer_id="Trainer 1"))
self.assertDatasetProduces(dataset1.take(10), list(range(10)))

dataset2 = self.make_distributed_dataset(
    dataset,
    cluster,
    job_name="job2",
    cross_trainer_cache=data_service_ops.CrossTrainerCache(
        trainer_id="Trainer 2"))
self.assertDatasetProduces(dataset2.take(10), list(range(10)))
