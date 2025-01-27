# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/session_support.py
"""Construct a heartbeat manager for the given devices."""
if not devices:
    logging.error('Trying to create heartbeat manager with no devices?')

logging.info('Creating heartbeat manager for %s', devices)
request_placeholder = array_ops.placeholder(
    name='worker_heartbeat_request', dtype=dtypes.string)

heartbeat_ops = []
for device in devices:
    with ops.device(device):
        heartbeat_ops.append(tpu_ops.worker_heartbeat(request_placeholder))

exit(WorkerHeartbeatManager(session, devices, heartbeat_ops,
                              request_placeholder))
