# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
local_resolver = SimpleClusterResolver(ClusterSpec({}), master='local')
remote.connect_to_cluster(local_resolver)
