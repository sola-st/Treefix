# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/cross_trainer_cache_test.py
cluster = self._create_cluster(
    num_workers=1, cross_trainer_cache_size_bytes=500)
dataset = dataset_ops.Dataset.range(10000000).repeat()
dataset1 = self.make_distributed_dataset(
    dataset,
    cluster,
    job_name="job",
    cross_trainer_cache=data_service_ops.CrossTrainerCache(
        trainer_id="Trainer 1"))
self.assertDatasetProduces(dataset1.take(200), list(range(200)))

dataset2 = self.make_distributed_dataset(
    dataset,
    cluster,
    job_name="job",
    cross_trainer_cache=data_service_ops.CrossTrainerCache(
        trainer_id="Trainer 2"))
dataset2 = dataset2.take(200)
output = self.getDatasetOutput(dataset2)
# When the cache is small, the second trainer couldn't read the beginning of
# the dataset. It can still read 200 elements from the dataset, because the
# dataset is infinite.
self.assertGreater(output[0], 0)
self.assertLen(output, 200)
