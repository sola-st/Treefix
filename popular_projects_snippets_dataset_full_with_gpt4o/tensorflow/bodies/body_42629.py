# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
super(MultiWorkersTest, self).setUp()

workers, _ = test_util.create_local_cluster(3, 0)
remote.connect_to_remote_host(
    [workers[0].target, workers[1].target, workers[2].target])
