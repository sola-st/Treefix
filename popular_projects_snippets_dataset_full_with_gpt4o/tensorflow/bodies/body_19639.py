# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client.py
if isinstance(tpu, list):
    if not tpu:
        raise ValueError('At least one TPU must be specified.')
    if len(tpu) != 1:
        raise NotImplementedError(
            'Using multiple TPUs in a single session is not yet implemented')
    tpu = tpu[0]

tpu = _get_tpu_name(tpu)

if tpu is None:
    tpu_node_config = _get_tpu_node_config()
    if tpu_node_config:
        tpu = tpu_node_config.get('tpu_node_name')
        project = project or tpu_node_config.get('project')
        zone = zone or tpu_node_config.get('zone')
    else:
        raise ValueError('Please provide a TPU Name to connect to.')

self._tpu = _as_text(tpu)

self._use_api = not self._tpu.startswith('grpc://')
self._service = service

self._credentials = None
self._project = None
self._zone = None
self._discovery_url = None
if self._use_api:
    if credentials != 'default':
        self._credentials = credentials
    # Automatically detect project and zone if unspecified.
    if project:
        self._project = _as_text(project)
    else:
        self._project = _request_compute_metadata('project/project-id')
    if zone:
        self._zone = _as_text(zone)
    else:
        zone_path = _request_compute_metadata('instance/zone')
        self._zone = zone_path.split('/')[-1]
    self._discovery_url = _environment_discovery_url() or discovery_url
