# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/worker_tags_test.py
with self.assertRaisesRegex(RuntimeError, "Worker tags cannot be empty."):
    _ = multi_process_cluster.MultiProcessCluster(
        num_local_workers=1,
        num_remote_workers=3,
        worker_tags=["", _COLOCATED_WORKER_TAG])
