# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
"""Creates a directory and all parent/intermediate directories.

  It succeeds if dirname already exists and is writable.

  Args:
    dirname: string, name of the directory to be created

  Raises:
    errors.OpError: If the operation fails.
  """
recursive_create_dir_v2(dirname)
