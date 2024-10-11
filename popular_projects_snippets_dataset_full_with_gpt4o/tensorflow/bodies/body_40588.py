# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_cluster_test.py
super(DynamicClusterTest, self).tearDown()
ops.device(None).__enter__()
context._reset_context()
