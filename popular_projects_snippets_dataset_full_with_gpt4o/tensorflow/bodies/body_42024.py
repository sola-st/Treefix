# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/device_placement_test.py
super(ClusterPlacementTest, self).setUp()
context._reset_context()
config.set_soft_device_placement(enabled=True)
context.context().log_device_placement = True
workers, _ = test_util.create_local_cluster(2, 0)
remote.connect_to_remote_host([workers[0].target, workers[1].target])
