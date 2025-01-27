# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/dtensor_device.py
"""Sets the singleton global device ID-to-physical core ID map.

    Args:
      mesh_name: The name of a mesh. If empty, set the default mapping.
      tpu_core_ids: TPU core IDs sorted by TF task/device ordinal.
    """
_pywrap_dtensor_device.SetTPUCoreIDs(self._device_info, mesh_name,
                                     tpu_core_ids)
