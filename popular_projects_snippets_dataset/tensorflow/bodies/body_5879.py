# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/kubernetes_cluster_resolver.py
"""Initializes a new KubernetesClusterResolver.

    This initializes a new Kubernetes ClusterResolver. The ClusterResolver
    will attempt to talk to the Kubernetes master to retrieve all the instances
    of pods matching a label selector.

    Args:
      job_to_label_mapping: A mapping of TensorFlow jobs to label selectors.
        This allows users to specify many TensorFlow jobs in one Cluster
        Resolver, and each job can have pods belong with different label
        selectors. For example, a sample mapping might be
        ```
        {'worker': ['job-name=worker-cluster-a', 'job-name=worker-cluster-b'],
         'ps': ['job-name=ps-1', 'job-name=ps-2']}
        ```
      tf_server_port: The port the TensorFlow server is listening on.
      rpc_layer: (Optional) The RPC layer TensorFlow should use to communicate
        between tasks in Kubernetes. Defaults to 'grpc'.
      override_client: The Kubernetes client (usually automatically retrieved
        using `from kubernetes import client as k8sclient`). If you pass this
        in, you are responsible for setting Kubernetes credentials manually.

    Raises:
      ImportError: If the Kubernetes Python client is not installed and no
        `override_client` is passed in.
      RuntimeError: If autoresolve_task is not a boolean or a callable.
    """
try:
    from kubernetes import config as k8sconfig  # pylint: disable=g-import-not-at-top

    k8sconfig.load_kube_config()
except ImportError:
    if not override_client:
        raise ImportError('The Kubernetes Python client must be installed '
                          'before using the Kubernetes Cluster Resolver. '
                          'To install the Kubernetes Python client, run '
                          '`pip install kubernetes` on your command line.')

if not job_to_label_mapping:
    job_to_label_mapping = {'worker': ['job-name=tensorflow']}

self._job_to_label_mapping = job_to_label_mapping
self._tf_server_port = tf_server_port
self._override_client = override_client

self.task_type = None
self.task_id = None
self.rpc_layer = rpc_layer
