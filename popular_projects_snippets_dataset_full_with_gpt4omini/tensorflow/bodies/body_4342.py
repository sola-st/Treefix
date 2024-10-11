# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/api.py
global _dtensor_singleton
if _dtensor_singleton is not None:
    _dtensor_singleton.clear_tpu_core_ids()
with _dtensor_singleton_lock:
    _dtensor_singleton = None
