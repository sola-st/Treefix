# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/sagemaker_cluster_resolver.py
"""Creates a new SageMakerClusterResolver.

    Args:
      port: (integer, optional) Override default port usage of 2223
      task_type: (String, optional) Overrides the task type.
      task_id: (Integer, optional) Overrides the task index.
      rpc_layer: (String, optional) Overrides the rpc layer TensorFlow uses.
      environment: (String, optional) Overrides the environment TensorFlow
        operates in.
    """
self._task_type = task_type
self._task_id = task_id
self._rpc_layer = rpc_layer
self._environment = environment
self._port = str(port)
