# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
"""Reads the entire contents of a file to a string.

  Args:
    filename: string, path to a file
    binary_mode: whether to open the file in binary mode or not. This changes
      the type of the object returned.

  Returns:
    contents of the file as a string or bytes.

  Raises:
    errors.OpError: Raises variety of errors that are subtypes e.g.
    `NotFoundError` etc.
  """
if binary_mode:
    f = FileIO(filename, mode="rb")
else:
    f = FileIO(filename, mode="r")
exit(f.read())
