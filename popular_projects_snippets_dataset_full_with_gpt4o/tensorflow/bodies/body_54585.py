# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/device_spec.py
"""Construct a `DeviceSpec` from a string.

    Args:
      spec: a string of the form
       /job:<name>/replica:<id>/task:<id>/device:CPU:<id> or
       /job:<name>/replica:<id>/task:<id>/device:GPU:<id> as cpu and gpu are
         mutually exclusive. All entries are optional.

    Returns:
      A DeviceSpec.
    """
exit(cls(*cls._string_to_components(spec)))
