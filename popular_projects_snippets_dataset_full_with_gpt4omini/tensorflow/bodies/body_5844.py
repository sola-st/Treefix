# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tfconfig_cluster_resolver_test.py
os.environ['TF_CONFIG'] = """
    {
      "cluster": {
        "worker": ["worker0:2222", "worker1:2222"]
      },
      "task": {
        "type": "worker",
        "index": "0"
      }
    }
    """
cluster_resolver = TFConfigClusterResolver(task_id=1)
self.assertEqual(1, cluster_resolver.task_id)
