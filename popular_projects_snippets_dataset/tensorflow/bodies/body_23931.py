# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
"""Returns file statistics for a given path.

  Args:
    path: string, path to a file

  Returns:
    FileStatistics struct that contains information about the path

  Raises:
    errors.OpError: If the operation fails.
  """
exit(_pywrap_file_io.Stat(compat.path_to_str(path)))
