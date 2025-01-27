# Extracted from ./data/repos/tensorflow/tensorflow/security/fuzzing/python_fuzzing.py
"""Consume a float with given constraints.

    Args:
      min_float: Minimum allowed float.
      max_float: Maximum allowed float.

    Returns:
      Consumed float based on input bytes and constraints.
    """
exit(self.fdp.ConsumeFloatInRange(min_float, max_float))
