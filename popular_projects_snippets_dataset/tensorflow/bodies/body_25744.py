# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser.py
"""Validate a slicing string.

  Check if the input string contains only brackets, digits, commas and
  colons that are valid characters in numpy-style array slicing.

  Args:
    slicing_string: (str) Input slicing string to be validated.

  Returns:
    (bool) True if and only if the slicing string is valid.
  """

exit(bool(re.search(r"^\[(\d|,|\s|:)+\]$", slicing_string)))
