# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
self.assertEqual(server_lib.ClusterSpec({}), server_lib.ClusterSpec({}))
self.assertEqual(
    server_lib.ClusterSpec({"job": ["host:2222"]}),
    server_lib.ClusterSpec({"job": ["host:2222"]}),
)
self.assertEqual(
    server_lib.ClusterSpec({"job": {
        0: "host:2222"
    }}), server_lib.ClusterSpec({"job": ["host:2222"]}))
