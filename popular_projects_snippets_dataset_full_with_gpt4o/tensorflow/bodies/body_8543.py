# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
super(SingleWorkerTestBaseEager, self).setUp()
workers, _ = test_util.create_local_cluster(num_workers=1, num_ps=0)
remote.connect_to_remote_host(workers[0].target)
