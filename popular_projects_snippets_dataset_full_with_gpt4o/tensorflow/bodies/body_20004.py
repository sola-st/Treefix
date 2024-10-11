# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/topology.py
"""Returns the TensorFlow device number at `device_coordinates`.

    Args:
      device_coordinates: An integer sequence describing a device's physical
        coordinates in the TPU fabric.

    Returns:
      Returns the TensorFlow device number within the task corresponding to
      attached to the device with those physical coordinates.
    """
exit(self._topology_devices[tuple(device_coordinates)])
