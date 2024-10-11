# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/local_workers_test.py
num_local_workers, num_remote_workers = (3, 3)
cluster = multi_process_cluster.MultiProcessCluster(num_local_workers,
                                                    num_remote_workers)
num_elements = 10
ds = dataset_ops.Dataset.range(num_elements)
datasets = {
    target_workers: self.make_distributed_dataset(
        ds, cluster, target_workers=target_workers)
    for target_workers in ["AUTO", "ANY", "LOCAL"]
}

num_workers = num_local_workers + num_remote_workers
self.assertDatasetProduces(
    datasets["AUTO"],
    num_workers * list(range(num_elements)),
    assert_items_equal=True)
self.assertDatasetProduces(
    datasets["ANY"],
    num_workers * list(range(num_elements)),
    assert_items_equal=True)
self.assertDatasetProduces(
    datasets["LOCAL"],
    num_local_workers * list(range(num_elements)),
    assert_items_equal=True)
