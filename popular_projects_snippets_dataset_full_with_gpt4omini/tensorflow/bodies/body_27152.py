# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/local_workers_test.py
cluster = multi_process_cluster.MultiProcessCluster(
    num_local_workers=num_local_workers,
    num_remote_workers=num_remote_workers)
num_elements = 10
num_repetitions = 5
ds = self.make_distributed_range_dataset(
    num_elements, cluster, target_workers="LOCAL")
ds = ds.repeat(num_repetitions)
self.assertDatasetProduces(
    ds,
    expected_output=num_local_workers * num_repetitions *
    list(range(num_elements)),
    assert_items_equal=True)
