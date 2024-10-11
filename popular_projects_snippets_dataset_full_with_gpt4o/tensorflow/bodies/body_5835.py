# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tfconfig_cluster_resolver_test.py
os.environ['TF_CONFIG'] = """
    {
      "cluster": {
        "ps": ["ps0:2222", "ps1:2222"],
        "worker": {"1": "worker1:2222"}
      },
      "task": {
        "type": "worker",
        "index": 1
      }
    }
    """

cluster_resolver = TFConfigClusterResolver()
expected_proto = """
    job { name: 'ps' tasks { key: 0 value: 'ps0:2222' }
                     tasks { key: 1 value: 'ps1:2222' } }
    job { name: 'worker' tasks { key: 1 value: 'worker1:2222' } }
    """
actual_cluster_spec = cluster_resolver.cluster_spec()
self._verifyClusterSpecEquality(actual_cluster_spec, expected_proto)
