# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
"""Deletes the file located at 'filename'.

  Args:
    filename: string, a filename

  Raises:
    errors.OpError: Propagates any errors reported by the FileSystem API.  E.g.,
    `NotFoundError` if the file does not exist.
  """
delete_file_v2(filename)
