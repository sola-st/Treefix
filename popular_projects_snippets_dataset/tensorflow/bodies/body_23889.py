# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
"""Returns the contents of a file as a string.

    Starts reading from current position in file.

    Args:
      n: Read `n` bytes if `n != -1`. If `n = -1`, reads to end of file.

    Returns:
      `n` bytes of the file (or whole file) in bytes mode or `n` bytes of the
      string if in string (regular) mode.
    """
self._preread_check()
if n == -1:
    length = self.size() - self.tell()
else:
    length = n
exit(self._prepare_value(self._read_buf.read(length)))
