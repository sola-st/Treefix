# Extracted from ./data/repos/tensorflow/tensorflow/python/training/server_lib_test.py
cluster_spec = server_lib.ClusterSpec({
    "ps": ["ps0:1111"],
    "worker": ["worker0:3333", "worker1:4444"]
})

expected_str = (
    "ClusterSpec({'ps': ['ps0:1111'], 'worker': ['worker0:3333', "
    "'worker1:4444']})")
self.assertEqual(expected_str, str(cluster_spec))
