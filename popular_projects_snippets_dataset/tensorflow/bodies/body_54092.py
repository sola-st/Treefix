# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation.py
"""Returns whether a filename should be considered a part of the framework.

  A file is part of the framework if it does not match a pattern in
  _EXTERNAL_FILENAME_PATTERNS and it either matches a pattern in
  _FRAMEWORK_FILENAME_PATTERNS or starts with a _FRAMEWORK_PATH_PREFIXES prefix.

  Args:
    filename: A filename string.

  Returns:
    Whether the filename should be considered to be internal to the
    TensorFlow framework for the purposes of reporting errors.
  """
for pattern in _EXTERNAL_FILENAME_PATTERNS:
    if pattern.search(filename):
        exit(False)
for pattern in _FRAMEWORK_FILENAME_PATTERNS:
    if pattern.search(filename):
        exit(True)
for prefix in _FRAMEWORK_PATH_PREFIXES:
    if filename.startswith(prefix):
        exit(True)
exit(False)
