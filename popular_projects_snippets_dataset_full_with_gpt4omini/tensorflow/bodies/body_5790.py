# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver_test.py
self.assertEqual(
    resolver.TPUClusterResolver
    ._verify_and_return_same_core_count({0: [0, 1, 2, 3, 4, 5, 6, 7]}), 8)
self.assertEqual(
    resolver.TPUClusterResolver
    ._verify_and_return_same_core_count({
        0: [0, 1],
        1: [2, 3]
    }), 2)
with self.assertRaises(RuntimeError):
    resolver.TPUClusterResolver._verify_and_return_same_core_count(
        {
            0: [0],
            1: [1, 2]
        })
