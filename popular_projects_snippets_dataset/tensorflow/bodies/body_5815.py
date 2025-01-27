# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/gce_cluster_resolver.py
"""Creates a new GCEClusterResolver object.

    This takes in a few parameters and creates a GCEClusterResolver project. It
    will then use these parameters to query the GCE API for the IP addresses of
    each instance in the instance group.

    Args:
      project: Name of the GCE project.
      zone: Zone of the GCE instance group.
      instance_group: Name of the GCE instance group.
      port: Port of the listening TensorFlow server (default: 8470)
      task_type: Name of the TensorFlow job this GCE instance group of VM
        instances belong to.
      task_id: The task index for this particular VM, within the GCE
        instance group. In particular, every single instance should be assigned
        a unique ordinal index within an instance group manually so that they
        can be distinguished from each other.
      rpc_layer: The RPC layer TensorFlow should use to communicate across
        instances.
      credentials: GCE Credentials. If nothing is specified, this defaults to
        GoogleCredentials.get_application_default().
      service: The GCE API object returned by the googleapiclient.discovery
        function. (Default: discovery.build('compute', 'v1')). If you specify a
        custom service object, then the credentials parameter will be ignored.

    Raises:
      ImportError: If the googleapiclient is not installed.
    """
self._project = project
self._zone = zone
self._instance_group = instance_group
self._task_type = task_type
self._task_id = task_id
self._rpc_layer = rpc_layer
self._port = port
self._credentials = credentials

if credentials == 'default':
    if _GOOGLE_API_CLIENT_INSTALLED:
        self._credentials = GoogleCredentials.get_application_default()

if service is None:
    if not _GOOGLE_API_CLIENT_INSTALLED:
        raise ImportError('googleapiclient must be installed before using the '
                          'GCE cluster resolver')
    self._service = discovery.build(
        'compute', 'v1',
        credentials=self._credentials)
else:
    self._service = service
