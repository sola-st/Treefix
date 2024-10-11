# Extracted from ./data/repos/tensorflow/tensorflow/security/fuzzing/python_fuzzing.py
"""Consume a signed integer with given constraints.

    Args:
      min_int: Minimum allowed integer.
      max_int: Maximum allowed integer.

    Returns:
      Consumed integer based on input bytes and constraints.
    """
exit(self.fdp.ConsumeIntInRange(min_int, max_int))
