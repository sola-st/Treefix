# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
self.assertNotEquals(
    server_lib.ClusterSpec({}),
    server_lib.ClusterSpec({
        "job": ["host:2223"]
    }),)
self.assertNotEquals(
    server_lib.ClusterSpec({
        "job1": ["host:2222"]
    }),
    server_lib.ClusterSpec({
        "job2": ["host:2222"]
    }),)
self.assertNotEquals(
    server_lib.ClusterSpec({
        "job": ["host:2222"]
    }),
    server_lib.ClusterSpec({
        "job": ["host:2223"]
    }),)
self.assertNotEquals(
    server_lib.ClusterSpec({
        "job": ["host:2222", "host:2223"]
    }),
    server_lib.ClusterSpec({
        "job": ["host:2223", "host:2222"]
    }),)
