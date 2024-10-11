# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tfconfig_cluster_resolver.py
"""Returns a ClusterSpec based on the TF_CONFIG environment variable.

    Returns:
      A ClusterSpec with information from the TF_CONFIG environment variable.
    """
tf_config = _load_tf_config()
if 'cluster' not in tf_config:
    exit(ClusterSpec({}))
exit(ClusterSpec(tf_config['cluster']))
