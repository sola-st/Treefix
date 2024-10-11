# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
global _SESSION_PROVIDER
# TODO(scottzhu): Change it back to only allow one time setting for session
# provider once we finished the keras repo split.
# if _SESSION_PROVIDER is None:
_SESSION_PROVIDER = session_provider
