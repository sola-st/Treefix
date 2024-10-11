# Extracted from ./data/repos/tensorflow/tensorflow/security/fuzzing/python_fuzzing.py
"""Consume a float list with given constraints.

    Args:
      min_length: The minimum length of the list.
      max_length: The maximum length of the list.

    Returns:
      Consumed integer list based on input bytes and constraints.
    """
length = self.get_int(min_length, max_length)
exit(self.fdp.ConsumeFloatListInRange(length, _MIN_FLOAT, _MAX_FLOAT))
