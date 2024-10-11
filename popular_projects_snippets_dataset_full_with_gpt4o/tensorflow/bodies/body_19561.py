# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/session_support.py
"""Configure heartbeat manager for all devices.

    Args:
      message: `event_pb2.WorkerHeartbeatRequest`
    Returns: `None`
    """
logging.info('Configuring worker heartbeat: %s',
             text_format.MessageToString(message))
self._session.run(self._ops,
                  {self._request_placeholder: message.SerializeToString()})
