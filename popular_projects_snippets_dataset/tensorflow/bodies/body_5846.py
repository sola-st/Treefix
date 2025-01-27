# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tfconfig_cluster_resolver_test.py
os.environ['TF_CONFIG'] = """
    {
      "cluster": {
        "worker": ["worker0:2222"]
      }
    }
    """

cluster_resolver = TFConfigClusterResolver()
self.assertEqual('', cluster_resolver.master())
