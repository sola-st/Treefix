# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/cross_trainer_cache_test.py
"""Tests cross-trainer cache with `register_dataset`/`from_dataset_id`."""
cluster = self._create_cluster(num_workers=1)
dataset = dataset_ops.Dataset.range(10000000).repeat()
dataset_id1 = data_service_ops.register_dataset(
    cluster.dispatcher.target, dataset, dataset_id="dataset_id")
dataset1 = data_service_ops.from_dataset_id(
    processing_mode=data_service_ops.ShardingPolicy.OFF,
    service=cluster.dispatcher.target,
    dataset_id=dataset_id1,
    element_spec=dataset.element_spec,
    job_name="job",
    cross_trainer_cache=data_service_ops.CrossTrainerCache(
        trainer_id="Trainer 1"))
self.assertDatasetProduces(dataset1.take(10), list(range(10)))

dataset_id2 = data_service_ops.register_dataset(
    cluster.dispatcher.target, dataset, dataset_id="dataset_id")
dataset2 = data_service_ops.from_dataset_id(
    processing_mode=data_service_ops.ShardingPolicy.OFF,
    service=cluster.dispatcher.target,
    dataset_id=dataset_id2,
    element_spec=dataset.element_spec,
    job_name="job",
    cross_trainer_cache=data_service_ops.CrossTrainerCache(
        trainer_id="Trainer 2"))
self.assertDatasetProduces(dataset2.take(10), list(range(10)))
