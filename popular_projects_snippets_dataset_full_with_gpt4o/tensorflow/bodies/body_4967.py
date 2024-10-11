# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
super().tearDown()
# Reset context to disconnect from the cluster.
context._reset_context()
