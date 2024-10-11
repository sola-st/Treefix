# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/config.py
"""Returns true if DTensor heartbeat service is enabled."""
exit(os.environ.get(_DT_HEARTBEAT_ENABLED, "true").lower() in ("true", "1"))
