# Extracted from ./data/repos/tensorflow/tensorflow/lite/ios/extract_object_files.py
"""Checks if the file has the correct archive header signature.

  The cursor is moved to the first available file header section after
  successfully checking the signature.

  Args:
    archive_file: The archive file object pointing at its beginning.

  Raises:
    RuntimeError: The archive signature is invalid.
  """
signature = archive_file.read(8)
if signature != b'!<arch>\n':
    raise RuntimeError('Invalid archive file format.')
