# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/worker_tags_test.py
cluster = multi_process_cluster.MultiProcessCluster(
    num_local_workers=1,
    num_remote_workers=3,
    worker_tags=["Unused tag 1", "Unused tag 2", "Unused tag 3"])
num_elements = 100
dataset = self.make_distributed_range_dataset(num_elements, cluster)
# The tags don't have an effect. tf.data service will read from all workers.
self.assertDatasetProduces(
    dataset, 4 * list(range(num_elements)), assert_items_equal=True)
