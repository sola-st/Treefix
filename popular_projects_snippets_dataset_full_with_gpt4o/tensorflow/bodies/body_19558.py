# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/session_support.py
"""Construct a new WorkerHeartbeatManager.

    (Prefer using `WorkerHeartbeatManager.from_devices` when possible.)

    Args:
      session: `tf.compat.v1.Session`, session to use for heartbeat operations.
      devices: `list[string]` Set of devices to connect to.
      heartbeat_ops: `list[tf.Operation]` Heartbeat operations.
      request_placeholder: `tf.Placeholder[String]` Placeholder used to specify
        the WorkerHeartbeatRequest protocol buffer.
    """
self._session = session
self._devices = devices
self._ops = heartbeat_ops
self._request_placeholder = request_placeholder
