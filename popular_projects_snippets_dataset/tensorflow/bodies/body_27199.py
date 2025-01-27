# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/cross_trainer_cache_ft_test.py
cluster = self._create_cluster(num_workers=1)
dataset = dataset_ops.Dataset.range(10000000).repeat()
distributed_dataset = self.make_distributed_dataset(
    dataset,
    cluster,
    job_name="job",
    cross_trainer_cache=data_service_ops.CrossTrainerCache(
        trainer_id="Trainer 1"))

get_next = self.getNext(distributed_dataset)
elements = self._get_next(get_next, 100)
self.assertEqual(elements, list(range(100)))

cluster.workers[0].restart()

# Read until we get results from the restarted worker, then read some more.
while self.evaluate(get_next()) != 0:
    pass

elements = self._get_next(get_next, 100)
self.assertEqual(elements, list(range(1, 101)))
