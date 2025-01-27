# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
# TODO(jhseu): Delete later. Used to omit `position` from docs.
# pylint: disable=g-doc-args
"""Seeks to the offset in the file.

    Args:
      offset: The byte count relative to the whence argument.
      whence: Valid values for whence are:
        0: start of the file (default)
        1: relative to the current position of the file
        2: relative to the end of file. `offset` is usually negative.
    """
# pylint: enable=g-doc-args
self._preread_check()
# We needed to make offset a keyword argument for backwards-compatibility.
# This check exists so that we can convert back to having offset be a
# positional argument.
# TODO(jhseu): Make `offset` a positional argument after `position` is
# deleted.
if offset is None and position is None:
    raise TypeError("seek(): offset argument required")
if offset is not None and position is not None:
    raise TypeError("seek(): offset and position may not be set "
                    "simultaneously.")

if position is not None:
    offset = position

if whence == 0:
    pass
elif whence == 1:
    offset += self.tell()
elif whence == 2:
    offset += self.size()
else:
    raise errors.InvalidArgumentError(
        None, None,
        "Invalid whence argument: {}. Valid values are 0, 1, or 2.".format(
            whence))
self._read_buf.seek(offset)
