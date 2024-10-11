# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
super(SingleWorkerTest, self).setUp()

workers, _ = test_util.create_local_cluster(1, 0)
remote.connect_to_remote_host(workers[0].target)
