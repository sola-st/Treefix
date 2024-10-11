# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_util_test.py
self.assertEqual(
    server_lib.ClusterSpec(lhs).as_dict(),
    server_lib.ClusterSpec(rhs).as_dict())
