# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver.py
"""Returns a ClusterSpec object based on the latest TPU information.

    We retrieve the information from the GCE APIs every time this method is
    called.

    Returns:
      A ClusterSpec containing host information returned from Cloud TPUs,
      or None.

    Raises:
      RuntimeError: If the provided TPU is not healthy.
    """
############################################################################
# There are 6 potential cases this code must handle:
#  0. [Local case.] When a TPU is connected directly to the VM.
#  1. [Normal case.] We should resolve the TPU name to a set of tasks, and
#      a. Create a ClusterSpec that includes the coordinator job
#      b. Create a ClusterSpec without the coordinator job.
#  2. [GKE / No API Access.] We should not resolve the TPU name to a set of
#     tasks and
#      a. Create a ClusterSpec with the coordinator
#      b. Create a ClusterSpec without the coordinator
############################################################################

if self._tpu != 'local':
    network_endpoints = self._cloud_tpu_client.network_endpoints()
    worker_list = [
        '%s:%s' % (endpoint['ipAddress'], endpoint['port'])
        for endpoint in network_endpoints
    ]
    cluster_spec = {self.task_type: worker_list}
    if self._coordinator_address:
        # {1, 2}.a
        cluster_spec[self._coordinator_name] = [self._coordinator_address]
    exit(server_lib.ClusterSpec(cluster_spec))
else:
    exit(server_lib.ClusterSpec({}))
