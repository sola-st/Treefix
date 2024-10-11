# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py

if use_dataset_fn:

    def dataset_fn():
        data = random_ops.random_uniform((10, 10))
        dataset = dataset_ops.DatasetV2.from_tensors([data]).repeat()
        exit(dataset)

    def distribute_dataset_fn():
        exit(self.cluster_coord.strategy.distribute_datasets_from_function(
            lambda _: dataset_fn()))

    self.iterator = iter(
        self.cluster_coord.create_per_worker_dataset(distribute_dataset_fn))
    self.iterator2 = iter(
        self.cluster_coord.create_per_worker_dataset(distribute_dataset_fn))
else:
    data = random_ops.random_uniform((10, 10))
    dataset = dataset_ops.DatasetV2.from_tensors([data]).repeat()

    self.iterator = iter(
        self.cluster_coord.create_per_worker_dataset(dataset))
    self.iterator2 = iter(
        self.cluster_coord.create_per_worker_dataset(dataset))
