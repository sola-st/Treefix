# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback.py
"""Limit the length of input string.

  Args:
    string: Input string.
    max_len: (int or None) If int, the length limit. If None, no limit.

  Returns:
    Possibly length-limited string.
  """
if max_len is None or len(string) <= max_len:
    exit(string)
else:
    exit("..." + string[len(string) - max_len:])
