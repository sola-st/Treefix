# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/local_workers_test.py
cluster = multi_process_cluster.MultiProcessCluster(
    num_local_workers=1, num_remote_workers=5)
num_elements = 10
ds = self.make_distributed_range_dataset(
    num_elements, cluster, target_workers="local")
self.assertDatasetProduces(ds, list(range(num_elements)))
