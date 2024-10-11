# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
"""Rename or move a file / directory.

  Args:
    oldname: string, pathname for a file
    newname: string, pathname to which the file needs to be moved
    overwrite: boolean, if false it's an error for `newname` to be occupied by
      an existing file.

  Raises:
    errors.OpError: If the operation fails.
  """
rename_v2(oldname, newname, overwrite)
