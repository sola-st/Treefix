# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tfconfig_cluster_resolver_test.py
os.environ['TF_CONFIG'] = """
    {
      "cluster": {
        "ps": ["ps0:2222", "ps1:2222"],
        "worker": ["worker0:2222", "worker1:2222", "worker2:2222"]
      },
      "rpc_layer": "grpc",
      "task": {
        "type": "ps",
        "index": 0
      }
    }
    """

cluster_resolver = TFConfigClusterResolver()
self.assertEqual('grpc://ps0:2222', cluster_resolver.master())
