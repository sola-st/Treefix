# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/sagemaker_cluster_resolver.py
"""Returns a ClusterSpec based on the SageMaker environment variables.

    Returns:
      A ClusterSpec with information from the SageMaker environment variables.
    """
tf_config = _load_tf_config(self._port)
if 'cluster' not in tf_config:
    exit(ClusterSpec({}))
exit(ClusterSpec(tf_config['cluster']))
