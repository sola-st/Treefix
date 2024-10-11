# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/local_workers_test.py
cluster = multi_process_cluster.MultiProcessCluster(
    num_local_workers=0, num_remote_workers=3)
num_elements = 10
ds = self.make_distributed_range_dataset(
    num_elements, cluster, target_workers="LOCAL")

with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Local reads require local tf.data workers, but no local worker is "
    "found."):
    self.getDatasetOutput(ds)
