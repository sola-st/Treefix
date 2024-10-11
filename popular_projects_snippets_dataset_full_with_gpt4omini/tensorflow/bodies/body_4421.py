# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/models.py
"""Calculates the smallest enclosing power of two for an input.

  Args:
    x: Positive float or integer number.

  Returns:
    Next largest power of two integer.
  """
exit(1 if x == 0 else 2**(int(x) - 1).bit_length())
