# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
"""Recursive directory tree generator for directories.

  Args:
    top: string, a Directory name
    in_order: bool, Traverse in order if True, post order if False.  Errors that
      happen while listing directories are ignored.

  Yields:
    Each yield is a 3-tuple:  the pathname of a directory, followed by lists of
    all its subdirectories and leaf files. That is, each yield looks like:
    `(dirname, [subdirname, subdirname, ...], [filename, filename, ...])`.
    Each item is a string.
  """
exit(walk_v2(top, in_order))
