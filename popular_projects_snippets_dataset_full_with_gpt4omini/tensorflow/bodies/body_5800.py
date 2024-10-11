# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tpu/tpu_cluster_resolver.py
"""Creates a new TPUClusterResolver object.

    The ClusterResolver will then use the parameters to query the Cloud TPU APIs
    for the IP addresses and ports of each Cloud TPU listed.

    Args:
      tpu: A string corresponding to the TPU to use. It can be the TPU name or
        TPU worker gRPC address. If not set, it will try automatically resolve
        the TPU address on Cloud TPUs. If set to "local", it will assume that
        the TPU is directly connected to the VM instead of over the network.
      zone: Zone where the TPUs are located. If omitted or empty, we will assume
        that the zone of the TPU is the same as the zone of the GCE VM, which we
        will try to discover from the GCE metadata service.
      project: Name of the GCP project containing Cloud TPUs. If omitted or
        empty, we will try to discover the project name of the GCE VM from the
        GCE metadata service.
      job_name: Name of the TensorFlow job the TPUs belong to.
      coordinator_name: The name to use for the coordinator. Set to None if the
        coordinator should not be included in the computed ClusterSpec.
      coordinator_address: The address of the coordinator (typically an ip:port
        pair). If set to None, a TF server will be started. If coordinator_name
        is None, a TF server will not be started even if coordinator_address is
        None.
      credentials: GCE Credentials. If None, then we use default credentials
        from the oauth2client
      service: The GCE API object returned by the googleapiclient.discovery
        function. If you specify a custom service object, then the credentials
        parameter will be ignored.
      discovery_url: A URL template that points to the location of the discovery
        service. It should have two parameters {api} and {apiVersion} that when
        filled in produce an absolute URL to the discovery document for that
        service. The environment variable 'TPU_API_DISCOVERY_URL' will override
        this.

    Raises:
      ImportError: If the googleapiclient is not installed.
      ValueError: If no TPUs are specified.
      RuntimeError: If an empty TPU name is specified and this is running in a
        Google Cloud environment.
    """

if tpu != 'local':
    # Default Cloud environment
    self._cloud_tpu_client = client.Client(
        tpu=tpu,
        zone=zone,
        project=project,
        credentials=credentials,
        service=service,
        discovery_url=discovery_url)
    self._tpu = self._cloud_tpu_client.name()
else:
    # Directly connected TPU environment
    self._cloud_tpu_client = _LocalCloudTpuClient()
    self._tpu = 'local'

# By default the task_type is 'worker` and the task_id is 0 (which is the
# first worker in the task).
self.task_type = job_name
self.task_id = 0
self._coordinator_name = coordinator_name
if (coordinator_name and not coordinator_address):
    self._start_local_server()
else:
    self._coordinator_address = coordinator_address

self._tpu_topology = None
