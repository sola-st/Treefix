# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver_test.py
with self.assertRaisesRegex(ValueError,
                            'Please provide a TPU Name to connect to.*'):
    resolver.TPUClusterResolver(tpu='')
