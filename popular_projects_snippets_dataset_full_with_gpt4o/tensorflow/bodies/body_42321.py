# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Set if soft device placements should be allowed.

  Args:
    enabled: Whether to enable soft device placement.
  """
context().soft_device_placement = enabled
