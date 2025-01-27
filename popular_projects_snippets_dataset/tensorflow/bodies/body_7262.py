# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_ops_test.py
cluster_spec_dict = multi_worker_test_base.create_cluster_spec(
    num_workers=num_processes)
self.runner = multi_process_runner.MultiProcessPoolRunner(cluster_spec_dict)
