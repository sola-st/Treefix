# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/session_support.py
self._saver = saver
self._checkpoint_prefix = checkpoint_prefix
self._on_shutdown_hooks = on_shutdown_hooks if on_shutdown_hooks else []

# Worker heartbeats are managed independently of the main training graph.
self._graph = ops.Graph()
self._workers = None
self._session = None
self._heartbeat_supported = False
