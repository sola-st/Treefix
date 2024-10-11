# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/topology.py
"""Returns the TensorFlow task number attached to `device_coordinates`.

    Args:
      device_coordinates: An integer sequence describing a device's physical
        coordinates in the TPU fabric.

    Returns:
      Returns the TensorFlow task number that contains the TPU device with those
      physical coordinates.
    """
exit(self._topology_tasks[tuple(device_coordinates)])
