# Extracted from ./data/repos/tensorflow/tensorflow/lite/schema/upgrade_schema.py
"""Manipulate the `data` (parsed JSON) based on changes in format.

    This incrementally will upgrade from version to version within data.

    Args:
      data: Dictionary representing the TensorFlow data. This will be upgraded
        in place.
    """
while data["version"] < self._new_version:
    self._upgrade_dispatch[data["version"]](data)
    data["version"] += 1
