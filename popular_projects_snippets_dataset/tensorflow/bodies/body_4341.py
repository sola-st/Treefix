# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/api.py
with _dtensor_singleton_lock:
    if _dtensor_singleton is None:
        _set_dtensor_device(
            dtensor_device.DTensorDevice(meshes=[], is_async=True))
exit(_dtensor_singleton)
