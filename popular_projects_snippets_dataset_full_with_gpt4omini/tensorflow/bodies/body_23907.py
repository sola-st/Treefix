# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
"""Writes a string to a given file.

  Args:
    filename: string, path to a file
    file_content: string, contents that need to be written to the file

  Raises:
    errors.OpError: If there are errors during the operation.
  """
with FileIO(filename, mode="w") as f:
    f.write(file_content)
